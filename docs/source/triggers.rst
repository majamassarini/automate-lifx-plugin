Triggers
********

Triggers are entities **comparable** with messages received from the Lifx bus.

If the comparison, made through the **is_triggered** method, returns True than the entity is considered to be triggered.

When the entity is triggered

1) if it is used by a **Scheduler Trigger** than its events are notified to *Appliances*
2) if it is used by a **Performer** its events are used to **directly** update an *Appliance*

.. autoclass:: lifx_plugin.trigger.Trigger

State
-----

.. autoclass:: lifx_plugin.trigger.State

