import sys
import datetime
import generation_commons as gc
import generate_sitemap
import generate_skeleton
import os

def main(argv):

    args = gc.parse_args(sys.argv)
    geoserver = args.geoserver
    sciencebase = args.sciencebase_url
    destination_dir = args.destination_dir
    gc.make_sure_path_exists(destination_dir)
    
    context = {
               'root_url' : args.root_url,
               'last_modified' : datetime.datetime.now().strftime('%Y-%m-%d')
               }
    data = gc.get_nwc_data(geoserver, sciencebase)

    generate_sitemap.generate_sitemap(data, os.path.join(destination_dir, 'sitemap'), context)
    generate_skeleton.generate_skeleton(data, os.path.join(destination_dir, 'skeleton'), context)
    
if __name__=="__main__":
    main(sys.argv)
    print 'Done'   
    
