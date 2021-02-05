import json
from operator import itemgetter
from pathlib import Path


# read json and return a scene dictionary, list of path to all the movie and movie with not-None scene
def data_preprocess(path_jsonfile):
    scene_val = []
    movie_w_scene = []
    movie_lst_all = []
    for jsonfile in path_jsonfile:
        movie_lst_all.append(jsonfile)
        sc = json.load(open(jsonfile, 'r'))
        if sc['scene'] is None:
            continue
        movie_w_scene.append(jsonfile)
        scene = []
        for x in sc['scene']:
            if x['shot'] is not None:
                temp_dict = {'id': sc['imdb_id'],
                             'shot': x['shot'],
                             'shot_idx': [],
                             'cast_tag': set(),
                             'action_tag': [],
                             'place_tag': []}
            if x['place_tag'] is not None:
                temp_dict['place_tag'].extend(x['place_tag'])
            if x['action_tag'] is not None:
                temp_dict['action_tag'].extend(list(map(itemgetter('tag'), x['action_tag'])))
            scene.append(temp_dict)

        if sc['cast']:
            cast = [{'shot_idx': x['shot_idx'],
                     'pid': x['pid']}
                    for x in sc['cast'] if x['pid'] and x['pid'] != 'others']
        else:
            cast = []

        k = 0
        for d in scene:
            i, j = d['shot']
            while k < len(cast):
                if i <= cast[k]['shot_idx'] < j:
                    d['cast_tag'].add(cast[k]['pid'])
                    d['shot_idx'].append(cast[k]['shot_idx'])
                    k += 1
                else:
                    break
        scene = [t for t in scene if t['cast_tag'] or t['action_tag'] or t['place_tag']]
        scene_val.append(scene)
    return scene_val, movie_w_scene, movie_lst_all


p = Path('/Users/jenniezhang/elvData/MovieNet/annotation')
p_lst = p.glob('*.json')