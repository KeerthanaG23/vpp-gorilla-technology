# vpp-gorilla-technology

Backend API development for VPP Commands and access the VPP CTL (CLI of VPP)

<!-- Reference Links -->

1. https://lists.fd.io/g/vpp-dev/topic/help_for_vpp_based_bgp/10640640?p=

2. https://haryachyy.wordpress.com/2020/04/17/learning-vpp-ospf-routing-protocol/

project_root/
│
├── vpp_clients/
│ ├── **init**.py
│ ├── interface_manager.py
│ ├── debug_client.py
│ ├── event_logger_client.py
│ ├── vlib_api_client.py
│ ├── vxlan_client.py
│ ├── plugin_clients/
│ │ ├── **init**.py
│ │ ├── ioam_client.py
│ │ ├── ila_client.py
│ │ ├── lb_client.py
│ │ ├── snat_client.py
│ │ ├── vcgn_client.py
│ │ └── ... (other plugins)
│ └── ...
│
├── main_application.py
└── other_modules/
└── ...
References:
https://chatgpt.com/share/6558808f-a438-49ae-8ec7-17ab12260ed6
