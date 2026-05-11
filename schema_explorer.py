# pipe the output of terraform providers schema -json to this code
import json
import sys  

schema=json.load(sys.stdin)

def print_block(block,indent=0):
    print(indent)
    indent_str=' '*indent
    if 'block' in block:
        for attr_name,attr in block['block']['attributes'].items():
            print(f"{indent_str}attribute: {attr_name}")
        for block_name,block in block['block']['block_types'].items():
            print(f"{indent_str}block: {block_name}")
            print_block(block,indent+2)
# print(type(schema))
# print(schema.keys())
ps=schema['provider_schemas']
# print(type(ps))
print(ps.keys())
l=schema['provider_schemas']['registry.terraform.io/linode/linode']
print(l.keys())
print(l['provider'].keys())
print()
print(l['resource_schemas'].keys())
print()
print(l['data_source_schemas'].keys())

# print_block(schema['provider_schemas']['registry.terraform.io/linode/linode']['provider'])
# print_block(schema['provider_schemas']['registry.terraform.io/linode/linode']['resource_schemas'])
# print_block(schema['provider_schemas']['registry.terraform.io/linode/linode']['data_source_schemas'])



rs=['linode_account_settings', 'linode_consumer_image_share_group_token', 'linode_database_access_controls', 'linode_database_mysql_v2', 
    'linode_database_postgresql_v2', 'linode_domain', 'linode_domain_record', 'linode_firewall', 'linode_firewall_device', 'linode_firewall_settings', 
    'linode_image', 'linode_instance', 'linode_instance_config', 'linode_instance_disk', 'linode_instance_ip', 'linode_instance_shared_ips', 'linode_interface', 
    'linode_ipv6_range', 'linode_lke_cluster', 'linode_lke_node_pool', 'linode_lock', 'linode_networking_ip', 'linode_networking_ip_assignment', 'linode_nodebalancer', 
    'linode_nodebalancer_config', 'linode_nodebalancer_node', 'linode_object_storage_bucket', 'linode_object_storage_key', 'linode_object_storage_object', 
    'linode_placement_group', 'linode_placement_group_assignment', 'linode_producer_image_share_group', 'linode_producer_image_share_group_member', 
    'linode_rdns', 'linode_reserved_ip_assignment', 'linode_sshkey', 'linode_stackscript', 'linode_token', 'linode_user', 'linode_volume', 'linode_vpc', 
    'linode_vpc_subnet']

ds=['linode_account', 'linode_account_availabilities', 'linode_account_availability', 'linode_account_login', 'linode_account_logins', 'linode_account_settings', 
    'linode_child_account', 'linode_child_accounts', 'linode_consumer_image_share_group', 'linode_consumer_image_share_group_image_shares', 'linode_consumer_image_share_group_token', 
    'linode_consumer_image_share_group_tokens', 'linode_database_engines', 'linode_database_mysql_config', 'linode_database_mysql_v2', 'linode_database_postgresql_config', 
    'linode_database_postgresql_v2', 'linode_databases', 'linode_domain', 'linode_domain_record', 'linode_domain_zonefile', 'linode_domains', 'linode_firewall', 
    'linode_firewall_settings', 'linode_firewall_template', 'linode_firewall_templates', 'linode_firewalls', 'linode_image', 'linode_images', 'linode_instance_backups', 
    'linode_instance_networking', 'linode_instance_type', 'linode_instance_types', 'linode_instances', 'linode_interface', 'linode_ipv6_range', 'linode_ipv6_ranges', 
    'linode_kernel', 'linode_kernels', 'linode_lke_cluster', 'linode_lke_clusters', 'linode_lke_node_pool', 'linode_lke_types', 'linode_lke_version', 'linode_lke_versions', 
    'linode_lock', 'linode_locks', 'linode_maintenance_policies', 'linode_nb_types', 'linode_network_transfer_prices', 'linode_networking_ip', 'linode_networking_ips', 
    'linode_nodebalancer', 'linode_nodebalancer_config', 'linode_nodebalancer_configs', 'linode_nodebalancer_node', 'linode_nodebalancer_vpc', 'linode_nodebalancer_vpcs', 
    'linode_nodebalancers', 'linode_object_storage_bucket', 'linode_object_storage_cluster', 'linode_object_storage_endpoints', 'linode_object_storage_quota', 'linode_object_storage_quotas', 
    'linode_placement_group', 'linode_placement_groups', 'linode_producer_image_share_group', 'linode_producer_image_share_group_image_shares', 'linode_producer_image_share_group_member', 
    'linode_producer_image_share_group_members', 'linode_producer_image_share_groups', 'linode_profile', 'linode_region', 'linode_region_vpc_availability', 'linode_regions', 
    'linode_regions_vpc_availability', 'linode_sshkey', 'linode_sshkeys', 'linode_stackscript', 'linode_stackscripts', 'linode_user', 'linode_users', 'linode_vlans', 
    'linode_volume', 'linode_volume_types', 'linode_volumes', 'linode_vpc', 'linode_vpc_ips', 'linode_vpc_subnet', 'linode_vpc_subnets', 'linode_vpcs']

r_target='linode_instance'
d_target='linode_instance_types'

import pprint

print()
print(l['resource_schemas'][r_target].keys())
pprint.pprint(l['resource_schemas'][r_target]['version'])
print(l['resource_schemas'][r_target]['block'].keys())
for key in l['resource_schemas'][r_target]['block']['attributes'].keys():
    print_string=f"***  {key}:"
    o=l['resource_schemas'][r_target]['block']['attributes'][key]
    computed=o.get('computed',False)
    required=o.get('required',False)
    optional=o.get('optional',False)
    print(required,optional,computed)
    if computed==False:
        if required and not optional:
            print_string+=' Pure Input'
        elif  not required and optional:
            print_string+=' Optional Input'
        else:
            print_string+=' UNDEFINED'
    else:
        if not required and not optional:
            print_string+=' Pure Output'
        elif not required and optional:
            print_string+=' Mixed Input/Output'
        else:
            print_string+=' UNDEFINED'

    # pprint.pprint({x:o[x] for x in o if 'description' not in x})
    print_string+=f"[type: {o['type']}]"
    print(print_string)
# print()
# print(l['data_source_schemas'][d_target].keys())
# pprint.pprint(l['data_source_schemas'][d_target]['version'])
# print(l['data_source_schemas'][d_target]['block'].keys())
# for key in l['data_source_schemas'][d_target]['block'].keys():
#     print(f"  {key}")
#     print(f"    {l['data_source_schemas'][d_target]['block'][key]}")
