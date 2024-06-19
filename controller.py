from flask import Flask, request, jsonify
import logging


from vpp.debug_client import DebugClient
from vpp.event_logger_client import EventLoggerClient
from vpp.interface_manager_client import InterfaceManagerClient
from vpp.vlib_api_client import VlibAPIClient
from vpp.vxlan_client import VxlanClient
from vpp.plugins.ila_lient import IlaClient
from vpp.plugins.ioam_client import IoamClient
from vpp.plugins.lb_client import LbClient
from vpp.plugins.snat_client import SnatClient
from vpp.plugins.vcgn_client import VcgnClient


from vpp.vnet.appacket_client import AppacketClient
from vpp.vnet.cdp_client import CdpClient
from vpp.vnet.classify_client import ClassifyClient
from vpp.vnet.cop_client import CopClient
from vpp.vnet.dhcp_client import DHCPClient
from vpp.vnet.dpdk_client import DDPdkClient
from vpp.vnet.flow_client import FlowClient
from vpp.vnet.gre_client import GreClient
from vpp.vnet.netmap_client import NetmapClient
from vpp.vnet.virtio_client import virtio_client
from vpp.vnet.vnet_client import VNetClient


# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


app = Flask(__name__)



# Initialize VPP clients
debug_client = DebugClient()
event_logger_client = EventLoggerClient()
interface_manager_client = InterfaceManagerClient()
vlib_api_client = VlibApiClient()
vxlan_client = VxlanClient()









