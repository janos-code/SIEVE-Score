from os.path import splitext
import numpy as np

from read_interaction import read_interaction
from scoring_noPCA import scoring_noPCA

def glide_KMeans_parameter(x):
    #read_interaction.py
    inter_array = np.array(read_interaction(x['i'],x['hits']))
    interactions = np.array(inter_array[1:,2:],dtype='float')

    #print(inter_array)
    #analyze, visualize

    sim = scoring_noPCA(inter_array,x['o'],x['p'],x['m'],x['propose'],
                        x['cutoff'],x['zeroneg'],
                        x['score_correction'],x['threshold'])
    #save_to_maegz(x['i'],labels,score)

    #plot(pca, inter_array, labels, x['cl'], x['o'],
            #x['skip'], x['title'], x['show'])

    print('\n*****Process Complete.*****\n')
    with open(splitext(x['o'])[0]+'.log','a') as f_log:
        f_log.write('\n*****Process Complete.*****\n')


if __name__ == '__main__':
    import sys
    from options import Input_func as Input

    #options.py
    default_option = {'i': [], 'o': None, 'hits': 'hits.txt',
                      'cl': 5, 'skip': 1, 'title': None,
                      'p': 1, 'm': -1, 'propose': 1000, 'show': True,
                      'score': True, 'zeroneg':False, 'score_correction':False,
                      'cutoff': 1, 'threshold': 1.0, 'p_opt': False,
                      'f_active':None}

    if "-file" in sys.argv:
        option_file = sys.argv[sys.argv.index("-file") + 1]
        o = open(option_file, 'r').readlines()
        o = [_.replace("\n","") for _ in o]
        o = o + sys.argv
    else:
        o = sys.argv

    option = Input(default_option,o)

    x = option
    with open(splitext(x['o'])[0]+'.log','w') as f_log:
        f_log.write('options:\n'+str(x)+'\n')

    glide_KMeans_parameter(x)
