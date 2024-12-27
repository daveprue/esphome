import esphome.codegen as cg
import esphome.config_validation as cv
from esphome import automation
from esphome.components import output
from esphome.const import CONF_ID, CONF_VALUE
from .. import PIPSOLAR_COMPONENT_SCHEMA, CONF_PIPSOLAR_ID, pipsolar_ns

DEPENDENCIES = ["pipsolar"]

PipsolarOutput = pipsolar_ns.class_("PipsolarOutput", output.FloatOutput)
SetOutputAction = pipsolar_ns.class_("SetOutputAction", automation.Action)

CONF_POSSIBLE_VALUES = "possible_values"

# 3.11 PCVV<nn.n><cr>: Setting battery C.V. (constant voltage) charging voltage 48.0V ~ 58.4V for 48V unit
# battery_bulk_voltage;
# battery_recharge_voltage;     12V unit: 11V/11.3V/11.5V/11.8V/12V/12.3V/12.5V/12.8V
#                               24V unit: 22V/22.5V/23V/23.5V/24V/24.5V/25V/25.5V
#                               48V unit: 44V/45V/46V/47V/48V/49V/50V/51V
# battery_under_voltage;        40.0V ~ 48.0V for 48V unit
# battery_float_voltage;        48.0V ~ 58.4V for 48V unit
# battery_type;  00 for AGM, 01 for Flooded battery
# current_max_ac_charging_current;
# output_source_priority; 00 / 01 / 02
# charger_source_priority;  For HS: 00 for utility first, 01 for solar first, 02 for solar and utility, 03 for only solar charging
#                           For MS/MSX: 00 for utility first, 01 for solar first, 03 for only solar charging
# battery_redischarge_voltage;  12V unit: 00.0V12V/12.3V/12.5V/12.8V/13V/13.3V/13.5V/13.8V/14V/14.3V/14.5
#                               24V unit: 00.0V/24V/24.5V/25V/25.5V/26V/26.5V/27V/27.5V/28V/28.5V/29V
#                               48V unit: 00.0V48V/49V/50V/51V/52V/53V/54V/55V/56V/57V/58V

CONF_BATTERY_RECHARGE_VOLTAGE = "battery_recharge_voltage"
CONF_BATTERY_UNDER_VOLTAGE = "battery_under_voltage"
CONF_BATTERY_BULK_VOLTAGE = "battery_bulk_voltage"
CONF_BATTERY_FLOAT_VOLTAGE = "battery_float_voltage"
CONF_BATTERY_TYPE = "battery_type"
CONF_CURRENT_MAX_AC_CHARGING_CURRENT = "current_max_ac_charging_current"
CONF_CURRENT_MAX_CHARGING_CURRENT = "current_max_charging_current"
CONF_OUTPUT_SOURCE_PRIORITY = "output_source_priority"
CONF_CHARGER_SOURCE_PRIORITY = "charger_source_priority"
CONF_BATTERY_REDISCHARGE_VOLTAGE = "battery_redischarge_voltage"
CONF_INPUT_VOLTAGE_RANGE = "input_voltage_range"
CONF_ENABLE_RESTART_ON_OVERLOAD = "enable_restart_on_overload"
CONF_DISABLE_RESTART_ON_OVERLOAD = "disable_restart_on_overload"
CONF_ENABLE_BYPASS_ON_OVERLOAD = "enable_bypass_on_overload"
CONF_DISABLE_BYPASS_ON_OVERLOAD = "disable_bypass_on_overload"
CONF_ENABLE_MENU_RETURNS_HOME = "enable_menu_returns_home"
CONF_DISABLE_MENU_RETURNS_HOME = "disable_menu_returns_home"
CONF_ENABLE_RESTART_ON_OVER_TEMP = "enable_restart_on_over_temp"
CONF_DISABLE_RESTART_ON_OVER_TEMP = "disable_restart_on_over_temp"

TYPES = {
    CONF_BATTERY_BULK_VOLTAGE: (
        [48.0, 48.1, 48.2, 48.3, 48.4, 48.5, 48.6, 48.7, 48.8, 48.9, 
         49.0, 49.1, 49.2, 49.3, 49.4, 49.5, 49.6, 49.7, 49.8, 49.9, 
         50.0, 50.1, 50.2, 50.3, 50.4, 50.5, 50.6, 50.7, 50.8, 50.9, 
         51.0, 51.1, 51.2, 51.3, 51.4, 51.5, 51.6, 51.7, 51.8, 51.9, 
         52.0, 52.1, 52.2, 52.3, 52.4, 52.5, 52.6, 52.7, 52.8, 52.9, 
         53.0, 53.1, 53.2, 53.3, 53.4, 53.5, 53.6, 53.7, 53.8, 53.9, 
         54.0, 54.1, 54.2, 54.3, 54.4, 54.5, 54.6, 54.7, 54.8, 54.9, 
         55.0, 55.1, 55.2, 55.3, 55.4, 55.5, 55.6, 55.7, 55.8, 55.9, 
         56.0, 56.1, 56.2, 56.3, 56.4, 56.5, 56.6, 56.7, 56.8, 56.9, 
         57.0, 57.1, 57.2, 57.3, 57.4, 57.5, 57.6, 57.7, 57.8, 57.9, 
         58.0, 58.1, 58.2, 58.3, 58.4, 58.5, 58.6, 58.7, 58.8, 58.9, 
         59.0, 59.1, 59.2, 59.3, 59.4, 59.5, 59.6, 59.7, 59.8, 59.9, 
         60.0, 60.1, 60.2, 60.3, 60.4, 60.5, 60.6, 60.7, 60.8, 60.9, 
         61.0, 61.1, 61.2, 61.3, 61.4, 61.5, 61.6, 61.7, 61.8, 61.9, 62.0], 
        "PCVV%02.1f"),
    CONF_BATTERY_FLOAT_VOLTAGE: (
        [48.0, 48.1, 48.2, 48.3, 48.4, 48.5, 48.6, 48.7, 48.8, 48.9, 
         49.0, 49.1, 49.2, 49.3, 49.4, 49.5, 49.6, 49.7, 49.8, 49.9, 
         50.0, 50.1, 50.2, 50.3, 50.4, 50.5, 50.6, 50.7, 50.8, 50.9, 
         51.0, 51.1, 51.2, 51.3, 51.4, 51.5, 51.6, 51.7, 51.8, 51.9, 
         52.0, 52.1, 52.2, 52.3, 52.4, 52.5, 52.6, 52.7, 52.8, 52.9, 
         53.0, 53.1, 53.2, 53.3, 53.4, 53.5, 53.6, 53.7, 53.8, 53.9, 
         54.0, 54.1, 54.2, 54.3, 54.4, 54.5, 54.6, 54.7, 54.8, 54.9, 
         55.0, 55.1, 55.2, 55.3, 55.4, 55.5, 55.6, 55.7, 55.8, 55.9, 
         56.0, 56.1, 56.2, 56.3, 56.4, 56.5, 56.6, 56.7, 56.8, 56.9, 
         57.0, 57.1, 57.2, 57.3, 57.4, 57.5, 57.6, 57.7, 57.8, 57.9, 
         58.0, 58.1, 58.2, 58.3, 58.4, 58.5, 58.6, 58.7, 58.8, 58.9, 
         59.0, 59.1, 59.2, 59.3, 59.4, 59.5, 59.6, 59.7, 59.8, 59.9, 
         60.0, 60.1, 60.2, 60.3, 60.4, 60.5, 60.6, 60.7, 60.8, 60.9, 
         61.0, 61.1, 61.2, 61.3, 61.4, 61.5, 61.6, 61.7, 61.8, 61.9, 62.0], 
        "PBFT%02.1f"),
    CONF_BATTERY_UNDER_VOLTAGE: (
        [40.0, 40.1, 40.2, 40.3, 40.4, 40.5, 40.6, 40.7, 40.8, 40.9, 
         41.0, 41.1, 41.2, 41.3, 41.4, 41.5, 41.6, 41.7, 41.8, 41.9, 
         42.0, 42.1, 42.2, 42.3, 42.4, 42.5, 42.6, 42.7, 42.8, 42.9, 
         43.0, 43.1, 43.2, 43.3, 43.4, 43.5, 43.6, 43.7, 43.8, 43.9, 
         44.0, 44.1, 44.2, 44.3, 44.4, 44.5, 44.6, 44.7, 44.8, 44.9, 
         45.0, 45.1, 45.2, 45.3, 45.4, 45.5, 45.6, 45.7, 45.8, 45.9, 
         46.0, 46.1, 46.2, 46.3, 46.4, 46.5, 46.6, 46.7, 46.8, 46.9, 
         47.0, 47.1, 47.2, 47.3, 47.4, 47.5, 47.6, 47.7, 47.8, 47.9, 
         48.0, 48.1, 48.2, 48.3, 48.4, 48.5, 48.6, 48.7, 48.8, 48.9, 
         49.0, 49.1, 49.2, 49.3, 49.4, 49.5, 49.6, 49.7, 49.8, 49.9, 
         50.0, 50.1, 50.2, 50.3, 50.4, 50.5, 50.6, 50.7, 50.8, 50.9, 
         51.0, 51.1, 51.2, 51.3, 51.4, 51.5, 51.6, 51.7, 51.8, 51.9, 
         52.0, 52.1, 52.2, 52.3, 52.4, 52.5, 52.6, 52.7, 52.8, 52.9, 
         53.0, 53.1, 53.2, 53.3, 53.4, 53.5, 53.6, 53.7, 53.8, 53.9, 54.0],
        "PSDV%02.1f"),
    CONF_BATTERY_RECHARGE_VOLTAGE: (
        [44.0, 44.1, 44.2, 44.3, 44.4, 44.5, 44.6, 44.7, 44.8, 44.9, 
         45.0, 45.1, 45.2, 45.3, 45.4, 45.5, 45.6, 45.7, 45.8, 45.9, 
         46.0, 46.1, 46.2, 46.3, 46.4, 46.5, 46.6, 46.7, 46.8, 46.9, 
         47.0, 47.1, 47.2, 47.3, 47.4, 47.5, 47.6, 47.7, 47.8, 47.9, 
         48.0, 48.1, 48.2, 48.3, 48.4, 48.5, 48.6, 48.7, 48.8, 48.9, 
         49.0, 49.1, 49.2, 49.3, 49.4, 49.5, 49.6, 49.7, 49.8, 49.9, 
         50.0, 50.1, 50.2, 50.3, 50.4, 50.5, 50.6, 50.7, 50.8, 50.9, 
         51.0, 51.1, 51.2, 51.3, 51.4, 51.5, 51.6, 51.7, 51.8, 51.9, 
         52.0, 52.1, 52.2, 52.3, 52.4, 52.5, 52.6, 52.7, 52.8, 52.9, 
         53.0, 53.1, 53.2, 53.3, 53.4, 53.5, 53.6, 53.7, 53.8, 53.9,
         54.0, 54.1, 54.2, 54.3, 54.4, 54.5, 54.6, 54.7, 54.8, 54.9,
         55.0, 55.1, 55.2, 55.3, 55.4, 55.5, 55.6, 55.7, 55.8, 55.9,
         56.0, 56.1, 56.2, 56.3, 56.4, 56.5, 56.6, 56.7, 56.8, 56.9,
         57.0, 57.1, 57.2],
        "PBCV%02.1f"),
    CONF_BATTERY_REDISCHARGE_VOLTAGE: (
        [0, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62],
        "PBDV%02.1f"),
    CONF_INPUT_VOLTAGE_RANGE: (
        [0, 1],
        "PGR%02.0f"),
    CONF_BATTERY_TYPE: (
        [0, 1, 2], 
        "PBT%02.0f"),
    CONF_CURRENT_MAX_AC_CHARGING_CURRENT: (
        [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120], 
        "MUCHGC%03.0f"),
    CONF_CURRENT_MAX_CHARGING_CURRENT: (
        [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120], 
        "MCHGC%03.0f"),
    CONF_OUTPUT_SOURCE_PRIORITY: (
        [0, 1, 2], 
        "POP%02.0f"),
    CONF_CHARGER_SOURCE_PRIORITY: (
        [0, 1, 2, 3], 
        "PCP%02.0f"),
    CONF_ENABLE_RESTART_ON_OVERLOAD: (
        [0, 1],
        "PEu"),
    CONF_DISABLE_RESTART_ON_OVERLOAD: (
        [0, 1],
        "PDu"),
    CONF_ENABLE_BYPASS_ON_OVERLOAD: (
        [0, 1],
        "PEb"),
    CONF_DISABLE_BYPASS_ON_OVERLOAD: (
        [0, 1],
        "PDb"),
    CONF_ENABLE_MENU_RETURNS_HOME: (
        [0, 1],
        "PEk"),
    CONF_DISABLE_MENU_RETURNS_HOME: (
        [0, 1],
        "PDk"),
    CONF_ENABLE_RESTART_ON_OVER_TEMP: (
        [0, 1],
        "PEv"),
    CONF_DISABLE_RESTART_ON_OVER_TEMP: (
        [0, 1],
        "PDv"),
}

CONFIG_SCHEMA = PIPSOLAR_COMPONENT_SCHEMA.extend(
    {
        cv.Optional(type): output.FLOAT_OUTPUT_SCHEMA.extend(
            {
                cv.Required(CONF_ID): cv.declare_id(PipsolarOutput),
                cv.Optional(CONF_POSSIBLE_VALUES, default=values): cv.All(
                    cv.ensure_list(cv.positive_float), cv.Length(min=1)
                ),
            }
        )
        for type, (values, _) in TYPES.items()
    }
)


async def to_code(config):
    paren = await cg.get_variable(config[CONF_PIPSOLAR_ID])

    for type, (_, command) in TYPES.items():
        if type in config:
            conf = config[type]
            var = cg.new_Pvariable(conf[CONF_ID])
            await output.register_output(var, conf)
            cg.add(var.set_parent(paren))
            cg.add(var.set_set_command(command))
            if (CONF_POSSIBLE_VALUES) in conf:
                cg.add(var.set_possible_values(conf[CONF_POSSIBLE_VALUES]))


@automation.register_action(
    "output.pipsolar.set_level",
    SetOutputAction,
    cv.Schema(
        {
            cv.Required(CONF_ID): cv.use_id(CONF_ID),
            cv.Required(CONF_VALUE): cv.templatable(cv.positive_float),
        }
    ),
)
def output_pipsolar_set_level_to_code(config, action_id, template_arg, args):
    paren = yield cg.get_variable(config[CONF_ID])
    var = cg.new_Pvariable(action_id, template_arg, paren)
    template_ = yield cg.templatable(config[CONF_VALUE], args, float)
    cg.add(var.set_level(template_))
    yield var
