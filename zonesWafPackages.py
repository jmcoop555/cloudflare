#source ./cloudflare.env 
#!/usr/bin/env python
"""Cloudflare API code - example"""

from __future__ import print_function

import os
import sys
import re

sys.path.insert(0, os.path.abspath('..'))
import CloudFlare

def main():
    """Cloudflare API code - example"""
    
    # Grab the first argument, if there is one
    try:
        zone_name = sys.argv[1]
        params = {'name':zone_name, 'per_page':1}
    except IndexError:
        params = {'per_page':50}

    cf = CloudFlare.CloudFlare()

    # grab the zone identifier
    try:
        zones = cf.zones.get(params=params)
    except CloudFlare.exceptions.CloudFlareAPIError as e:
        exit('/zones %d %s - api call failed' % (e, e))
    except Exception as e:
        exit('/zones.get - %s - api call failed' % (e))

    # there should only be one zone
    for zone in sorted(zones, key=lambda v: v['name']):
        zone_name = zone['name']
        zone_id = zone['id']
        if 'email' in zone['owner']:
            zone_owner = zone['owner']['email']
        else:
            zone_owner = '"' + zone['owner']['name'] + '"'
            zone_plan = zone['plan']['name']

        print(zone_id, zone_name, zone_owner, zone_plan)

        try:
            packages = cf.zones.firewall.waf.packages.get(zone_id)  #firewall.waf.packages.rules
        except CloudFlare.exceptions.CloudFlareAPIError as e:
            exit('/zones.firewall.waf.packages.get %d %s - api call failed' % (e, e))

        for package in sorted(packages, key=lambda v: v['id']):
            p_id = package['id']
            p_name = package['name']
            p_descrip = package['description']
            p_detect = package['detection_mode']
            
            getZoneWafPackageDetails(zone_id,p_id,p_name)

        print('')

    exit(0)

def getZoneWafPackageDetails(zone_id,package_id,package_name):
    try:
        zone_name = sys.argv[1]
        params = {'name':zone_name, 'per_page':1}
    except IndexError:
        params = {'per_page':50}

    cf = CloudFlare.CloudFlare()

    try:
        rules = cf.zones.firewall.waf.packages.groups.get(zone_id, package_id)
        print('***************************')
        print('package_name: '+package_name)
        print('***************************')
    except CloudFlare.exceptions.CloudFlareAPIError as e:
        exit('/zones.firewall.waf.packages.rules.get %d %s - api call failed' % (e, e))

    for rule in sorted(rules, key=lambda v: v['id']):
        r_id = rule['id']
        r_name = rule['name']
        r_mode = rule['mode']

        print(r_id, r_name,"-- "+r_mode)

if __name__ == '__main__':
    main()
