from flask import Flask, request, jsonify
from flask_restx import Api, Resource, fields
import logging
from vpp.debug_client import DebugClient
from vpp.event_logger_client import EventLoggerClient
from vpp.interface_manager_client import InterfaceManagerClient  

app = Flask(__name__)
api = Api(app, version='1.0', title='VPP Management API', description='APIs for managing VPP operations')

# Configure logging
logging.basicConfig(filename='logs/vpppy.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

# Initialize clients
debug_client = DebugClient()
event_logger_client = EventLoggerClient()
interface_manager_client = InterfaceManagerClient()

# Define namespaces
debug_ns = api.namespace('debug', description='Debug Operations')
event_logger_ns = api.namespace('event-logger', description='Event Logger Operations')
interface_ns = api.namespace('interface', description='Interface Management Operations')


# DTOs (Data Transfer Objects) for request payloads
command_model = api.model('Command', {
    'command': fields.String(required=True, description='Command to execute')
})

size_model = api.model('Size', {
    'size': fields.Integer(required=True, description='Size for resizing event log')
})

filename_model = api.model('Filename', {
    'filename': fields.String(required=True, description='Filename for saving event log')
})

# Debug endpoints
@debug_ns.route('/execute')
class ExecuteCommand(Resource):
    @api.expect(command_model)
    def post(self):
        try:
            data = request.json
            command = data.get('command')
            if not command:
                raise ValueError("Command is required")
            output = debug_client.run_vpp_command(command)
            return {'output': output}
        except Exception as e:
            logging.exception(f"Error executing command: {e}")
            return {'error': str(e)}, 500

@debug_ns.route('/history')
class ShowCliHistory(Resource):
    def get(self):
        try:
            output = debug_client.show_cli_history()
            return {'output': output}
        except Exception as e:
            logging.exception(f"Error showing CLI history: {e}")
            return {'error': str(e)}, 500

@debug_ns.route('/quit')
class QuitCli(Resource):
    def get(self):
        try:
            output = debug_client.quit_cli()
            return {'output': output}
        except Exception as e:
            logging.exception(f"Error quitting CLI: {e}")
            return {'error': str(e)}, 500

@debug_ns.route('/terminal/ansi')
class SetTerminalAnsi(Resource):
    @api.expect(fields.Boolean)
    def post(self):
        try:
            data = request.json
            enable = data.get('enable', True)  # Default to True if not provided
            output = debug_client.set_terminal_ansi(enable)
            return {'output': output}
        except Exception as e:
            logging.exception(f"Error setting terminal ANSI: {e}")
            return {'error': str(e)}, 500

@debug_ns.route('/terminal/history')
class SetTerminalHistory(Resource):
    @api.expect(fields.Boolean)
    def post(self):
        try:
            data = request.json
            enable = data.get('enable', True)  # Default to True if not provided
            limit = data.get('limit')
            output = debug_client.set_terminal_history(enable, limit)
            return {'output': output}
        except Exception as e:
            logging.exception(f"Error setting terminal history: {e}")
            return {'error': str(e)}, 500

@debug_ns.route('/terminal/pager')
class SetTerminalPager(Resource):
    @api.expect(fields.Boolean)
    def post(self):
        try:
            data = request.json
            enable = data.get('enable', True)  # Default to True if not provided
            limit = data.get('limit')
            output = debug_client.set_terminal_pager(enable, limit)
            return {'output': output}
        except Exception as e:
            logging.exception(f"Error setting terminal pager: {e}")
            return {'error': str(e)}, 500

@debug_ns.route('/terminal/settings')
class ShowTerminalSettings(Resource):
    def get(self):
        try:
            output = debug_client.show_terminal_settings()
            return {'output': output}
        except Exception as e:
            logging.exception(f"Error showing terminal settings: {e}")
            return {'error': str(e)}, 500

@debug_ns.route('/unix-errors')
class ShowUnixErrors(Resource):
    def get(self):
        try:
            output = debug_client.show_unix_errors()
            return {'output': output}
        except Exception as e:
            logging.exception(f"Error showing Unix errors: {e}")
            return {'error': str(e)}, 500

# Event Logger endpoints
@event_logger_ns.route('/clear')
class ClearEventLog(Resource):
    def get(self):
        try:
            output = event_logger_client.clear_event_log()
            return {'output': output}
        except Exception as e:
            logging.exception(f"Error clearing event log: {e}")
            return {'error': str(e)}, 500

@event_logger_ns.route('/resize')
class ResizeEventLog(Resource):
    @api.expect(size_model)
    def post(self):
        try:
            data = request.json
            size = data.get('size')
            output = event_logger_client.resize_event_log(size)
            return {'output': output}
        except Exception as e:
            logging.exception(f"Error resizing event log: {e}")
            return {'error': str(e)}, 500

@event_logger_ns.route('/restart')
class RestartEventLogger(Resource):
    def get(self):
        try:
            output = event_logger_client.restart_event_logger()
            return {'output': output}
        except Exception as e:
            logging.exception(f"Error restarting event logger: {e}")
            return {'error': str(e)}, 500

@event_logger_ns.route('/save')
class SaveEventLog(Resource):
    @api.expect(filename_model)
    def post(self):
        try:
            data = request.json
            filename = data.get('filename')
            output = event_logger_client.save_event_log(filename)
            return {'output': output}
        except Exception as e:
            logging.exception(f"Error saving event log: {e}")
            return {'error': str(e)}, 500

@event_logger_ns.route('/stop')
class StopEventLogger(Resource):
    def get(self):
        try:
            output = event_logger_client.stop_event_logger()
            return {'output': output}
        except Exception as e:
            logging.exception(f"Error stopping event logger: {e}")
            return {'error': str(e)}, 500

@event_logger_ns.route('/info')
class ShowEventLoggerInfo(Resource):
    def get(self):
        try:
            output = event_logger_client.show_event_logger_info()
            return {'output': output}
        except Exception as e:
            logging.exception(f"Error showing event logger info: {e}")
            return {'error': str(e)}, 500

if __name__ == '__main__':
    app.run(debug=True)
