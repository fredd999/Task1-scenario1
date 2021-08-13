from ncclient import manager
from lxml import etree


def get_request(xmlstring):
    print("XML FILTER:")
    print(xmlstring)
    print("-" * 80)
    with manager.connect(host='10.0.0.111', port=830,
                         username='cisco', password='cisco',
                         hostkey_verify=False, device_params={},
                         allow_agent=False, look_for_keys=False) as device:
        netconf_get_reply = device.get(('subtree', xmlstring))
    ourput_file = etree.tostring(netconf_get_reply.data_ele, pretty_print=True).decode('utf-8')
    print("NETCONF RESPONSE:")
    print(ourput_file)
    print("=" * 80)
    print("=" * 80)
    print("=" * 80)


xml_filter = """ 
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native"> 
     <router> 
     </router> 
    </native> 
"""

print("NETCONF Result: ")
get_request(xml_filter)
print("*" * 80)
print("\n")


