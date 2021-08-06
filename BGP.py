from ncclient import manager
from jinja2 import Template


A = manager.connect(host='10.0.0.111', port=830, username='cisco',
                   password='cisco', device_params={'name': 'csr'})

bgp_template = Template(open('bgp.xml').read())
bgp_rendered = bgp_template.render(BGP_AS=input("Please specify local AS: "),
                                   NEIGHBOR_IP=input("enter neighbor IP address: "),
                                   REMOTE_AS=input("Enter Remote AS Number: "),
                                   UPDATE_INTERFACE=input("Enter Loopback ID: "))

Configuration = A.edit_config(target='running', config=bgp_rendered)
print(Configuration)

1