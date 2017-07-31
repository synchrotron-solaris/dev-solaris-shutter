"""
This module contains device class BeamEnergy and run method for it.
"""

# Imports
from tango import DevState, AttrWriteType, DispLevel
from facadedevice import Facade, proxy_attribute, proxy_command


class Shutter(Facade):
    """
    This class implements Tango device server for control of shutter device (integrated shutter and stopper).
    Each Tango device represents one shutter, which can be in open or closed.

    The Tango device works on a set of four PLC attributes of type DevShort, which must be
    exposed by PLC device server.

    OpenS PLC attribute should be True when shutter is open and False when it is closed
    ClosedS PLC attribute should be True when shutter is closed and False when it is opened

    OpenC PLC attribute should cause shutter to open if it is closed
    CloseC PLC attribute should cause shutter to close if it is open
    """

    def safe_init_device(self):
        """
        This is a method to safely initialize the Shutter device,
        overrode from Facade base class
        """
        super(Shutter, self).safe_init_device()
        self.set_state(DevState.ON)
        self.set_status("Device is running.")

    # proxy attributes

    ShutterOpen = proxy_attribute(
        dtype=bool,
        access=AttrWriteType.READ,
        property_name="PLCAttrName_OpenS",
        display_level=DispLevel.OPERATOR,
        description="Attribute that represents PLC signal for shutter open "
                    "state.")

    ShutterClosed = proxy_attribute(
        dtype=bool,
        access=AttrWriteType.READ,
        property_name="PLCAttrName_ClosedS",
        display_level=DispLevel.OPERATOR,
        description="Attribute that represents PLC signal for shutter closed "
                    "state.")

    ShutterInterlock = proxy_attribute(
        dtype=bool,
        access=AttrWriteType.READ,
        property_name="PLCAttrName_InterlockA",
        display_level=DispLevel.OPERATOR,
        description="Attribute that represents PLC signal for shutter in "
                    "interlock alarm.")

    # proxy commands

    @proxy_command(
        dtype_out=bool,
        write_attribute=True,
        property_name="PLCAttrName_OpenC",
        doc_out="True to PLCAttrName_OpenC")
    def Open(self, subcommand):
        """
         :rtype: bool
        """
        subcommand(1)
        return True

    @proxy_command(
        dtype_out=bool,
        write_attribute=True,
        property_name="PLCAttrName_CloseC",
        doc_out="True to PLCAttrName_CloseC")
    def Close(self, subcommand):
        """
        :rtype: bool
        """
        subcommand(1)
        return True

# run server

run = Shutter.run_server()

if __name__ == '__main__':
    run()
