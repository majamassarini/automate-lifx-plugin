Commands
********

Commands are entities **capable of forge** messages for the Lifx bus interpreting changes in *Appliance* state.

Commands *compare* an *old Appliance state* with a *new one* and create messages to be sent to the Appliance's device.

Commands are designed to read *Appliance's attributes*: :meth:`home.appliance.attribute.mixin`

.. autoclass:: lifx_plugin.message.Command

Set Color
---------

.. autoclass:: lifx_plugin.command.SetColor

Set Waveform
------------

.. autoclass:: lifx_plugin.command.SetWaveform
