from classes.logger import Logger
from classes.naked import Naked
from classes.proxymanager import ProxyManager

from os import listdir

def main():
    log = Logger().log
    proxy_manager = ProxyManager()
    log('******************************************************\n'
    
    
                                                 
'''
               )                                       )                                
            ( /(           )        (               ( /(                                
            )\())    )  ( /(    (   )\ )            )\()) (   (                         
   __ __ __((_)\  ( /(  )\())  ))\ (()/(   __ __ __((_)\  )\  )(    (    (     __ __ __ 
  / // // / _((_) )(_))((_)\  /((_) ((_)) / // // / _((_)((_)(()\   )\   )\   / // // / 
 / // // / | \| |((_)_ | |(_)(_))   _| | / // // / | \| | (_) ((_) ((_) ((_) / // // /  
/_//_//_/  | .` |/ _` || / / / -_)/ _` |/_//_//_/  | .` | | || '_|/ _ \/ _ \/_//_//_/   
           |_|\_|\__,_||_\_\ \___|\__,_|           |_|\_| |_||_|  \___/\___/            
                                                                                                                                                                                                                                   
'''
                                                 

        
        '\nCreated by Niroo @NirooOfficial'
        '\nCredits to Shevi @Shevids1996\n\n'
    
    
        '******************************************************', color='blue', timestamp=False)
    log('starting tasks', color='green')

    threads = []
    i = 0
    for task in listdir('tasks'):
        threads.append(Naked(i, 'tasks/{}'.format(task), proxy_manager))
        threads[i].start()
        i += 1

if __name__ == '__main__':
    main()
