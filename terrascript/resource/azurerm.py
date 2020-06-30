# terrascript/resource/azurerm.py

import terrascript


class azurerm_network_interface(terrascript.Resource):
    pass


class azurerm_windows_virtual_machine(terrascript.Resource):
    pass


class azurerm_linux_virtual_machine(terrascript.Resource):
    pass


class azurerm_network_interface_security_group_association(terrascript.Resource):
    pass


class azurerm_network_security_group(terrascript.Resource):
    pass


class azurerm_virtual_machine_extension(terrascript.Resource):
    pass


__all__ = [
    "azurerm_network_interface",
    "azurerm_windows_virtual_machine",
    "azurerm_linux_virtual_machine",
    "azurerm_network_security_group",
    "azurerm_network_interface_security_group_association",
    "azurerm_virtual_machine_extension"
]
