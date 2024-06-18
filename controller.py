# Designing endpoitns that reflects the functionality of VPP
from flask import Flask, request, jsonify
import logging


# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')



# Initialize Flask app 
app = Flask(__name__)


