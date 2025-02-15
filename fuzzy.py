import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl


hydraulic_performance = ctrl.Antecedent(np.arange(0, 1.01, 0.01), 'hydraulic_performance')
technical_condition = ctrl.Antecedent(np.arange(0, 1.01, 0.01), 'technical_condition')
operational_condition = ctrl.Antecedent(np.arange(0, 1.01, 0.01), 'operational_condition')
consequence = ctrl.Consequent(np.arange(0, 1.01, 0.01), 'consequence')

hydraulic_performance['very_poor'] = fuzz.zmf(hydraulic_performance.universe, 0.0, 0.3)
hydraulic_performance['poor'] = fuzz.pimf(hydraulic_performance.universe, 0.1, (0.1 + 0.5)/2, (0.1 + 0.5)/2, 0.5)
hydraulic_performance['fair'] = fuzz.pimf(hydraulic_performance.universe, 0.3, (0.3 + 0.7)/2, (0.3 + 0.7)/2, 0.7)
hydraulic_performance['good'] = fuzz.pimf(hydraulic_performance.universe, 0.5, (0.5 + 0.9)/2, (0.5 + 0.9)/2, 0.9)
hydraulic_performance['excellent'] = fuzz.smf(hydraulic_performance.universe, 0.7, 1.0)

technical_condition['very_poor'] = fuzz.zmf(technical_condition.universe, 0.0, 0.3)
technical_condition['poor'] = fuzz.pimf(technical_condition.universe, 0.1, (0.1 + 0.5)/2, (0.1 + 0.5)/2, 0.5)
technical_condition['fair'] = fuzz.pimf(technical_condition.universe, 0.3, (0.3 + 0.7)/2, (0.3 + 0.7)/2, 0.7)
technical_condition['good'] = fuzz.pimf(technical_condition.universe, 0.5, (0.5 + 0.9)/2, (0.5 + 0.9)/2, 0.9)
technical_condition['excellent'] = fuzz.smf(technical_condition.universe, 0.7, 1.0)

operational_condition['very_low'] = fuzz.zmf(operational_condition.universe, 0.0, 0.3)
operational_condition['low'] = fuzz.pimf(operational_condition.universe, 0.1, (0.1 + 0.5)/2, (0.1 + 0.5)/2, 0.5)
operational_condition['moderate'] = fuzz.pimf(operational_condition.universe, 0.3, (0.3 + 0.7)/2, (0.3 + 0.7)/2, 0.7)
operational_condition['high'] = fuzz.pimf(operational_condition.universe, 0.5, (0.5 + 0.9)/2, (0.5 + 0.9)/2, 0.9)
operational_condition['very_high'] = fuzz.smf(operational_condition.universe, 0.7, 1.0)

consequence['immediate_replacement'] = fuzz.zmf(consequence.universe, 0.0, 0.3)
consequence['major_rehabilitation'] = fuzz.pimf(consequence.universe, 0.1, (0.1 + 0.5)/2, (0.1 + 0.5)/2, 0.5)
consequence['routine_maintenance'] = fuzz.pimf(consequence.universe, 0.3, (0.3 + 0.7)/2, (0.3 + 0.7)/2, 0.7)
consequence['monitoring_only'] = fuzz.pimf(consequence.universe, 0.5, (0.5 + 0.9)/2, (0.5 + 0.9)/2, 0.9)
consequence['no_action'] = fuzz.smf(consequence.universe, 0.7, 1.0)

# Defining fuzzy rules for hydraulic_performance = very_poor

rule_1 = ctrl.Rule(hydraulic_performance['very_poor'] & technical_condition['very_poor'] & operational_condition['very_low'], consequence['immediate_replacement'])
rule_2 = ctrl.Rule(hydraulic_performance['very_poor'] & technical_condition['very_poor'] & operational_condition['low'], consequence['immediate_replacement'])
rule_3 = ctrl.Rule(hydraulic_performance['very_poor'] & technical_condition['very_poor'] & operational_condition['moderate'], consequence['immediate_replacement'])
rule_4 = ctrl.Rule(hydraulic_performance['very_poor'] & technical_condition['very_poor'] & operational_condition['high'], consequence['immediate_replacement'])
rule_5 = ctrl.Rule(hydraulic_performance['very_poor'] & technical_condition['very_poor'] & operational_condition['very_high'], consequence['immediate_replacement'])
rule_6 = ctrl.Rule(hydraulic_performance['very_poor'] & technical_condition['poor'] & operational_condition['very_low'], consequence['immediate_replacement'])
rule_7 = ctrl.Rule(hydraulic_performance['very_poor'] & technical_condition['poor'] & operational_condition['low'], consequence['major_rehabilitation'])
rule_8 = ctrl.Rule(hydraulic_performance['very_poor'] & technical_condition['poor'] & operational_condition['moderate'], consequence['major_rehabilitation'])
rule_9 = ctrl.Rule(hydraulic_performance['very_poor'] & technical_condition['poor'] & operational_condition['high'], consequence['major_rehabilitation'])
rule_10 = ctrl.Rule(hydraulic_performance['very_poor'] & technical_condition['poor'] & operational_condition['very_high'], consequence['major_rehabilitation'])
rule_11 = ctrl.Rule(hydraulic_performance['very_poor'] & technical_condition['fair'] & operational_condition['very_low'], consequence['major_rehabilitation'])
rule_12 = ctrl.Rule(hydraulic_performance['very_poor'] & technical_condition['fair'] & operational_condition['low'], consequence['major_rehabilitation'])
rule_13 = ctrl.Rule(hydraulic_performance['very_poor'] & technical_condition['fair'] & operational_condition['moderate'], consequence['major_rehabilitation'])
rule_14 = ctrl.Rule(hydraulic_performance['very_poor'] & technical_condition['fair'] & operational_condition['high'], consequence['major_rehabilitation'])
rule_15 = ctrl.Rule(hydraulic_performance['very_poor'] & technical_condition['fair'] & operational_condition['very_high'], consequence['major_rehabilitation'])
rule_16 = ctrl.Rule(hydraulic_performance['very_poor'] & technical_condition['good'] & operational_condition['very_low'], consequence['major_rehabilitation'])
rule_17 = ctrl.Rule(hydraulic_performance['very_poor'] & technical_condition['good'] & operational_condition['low'], consequence['major_rehabilitation'])
rule_18 = ctrl.Rule(hydraulic_performance['very_poor'] & technical_condition['good'] & operational_condition['moderate'], consequence['major_rehabilitation'])
rule_19 = ctrl.Rule(hydraulic_performance['very_poor'] & technical_condition['good'] & operational_condition['high'], consequence['major_rehabilitation'])
rule_20 = ctrl.Rule(hydraulic_performance['very_poor'] & technical_condition['good'] & operational_condition['very_high'], consequence['major_rehabilitation'])
rule_21 = ctrl.Rule(hydraulic_performance['very_poor'] & technical_condition['excellent'] & operational_condition['very_low'], consequence['major_rehabilitation'])
rule_22 = ctrl.Rule(hydraulic_performance['very_poor'] & technical_condition['excellent'] & operational_condition['low'], consequence['major_rehabilitation'])
rule_23 = ctrl.Rule(hydraulic_performance['very_poor'] & technical_condition['excellent'] & operational_condition['moderate'], consequence['major_rehabilitation'])
rule_24 = ctrl.Rule(hydraulic_performance['very_poor'] & technical_condition['excellent'] & operational_condition['high'], consequence['major_rehabilitation'])
rule_25 = ctrl.Rule(hydraulic_performance['very_poor'] & technical_condition['excellent'] & operational_condition['very_high'], consequence['major_rehabilitation'])

rule_26 = ctrl.Rule(hydraulic_performance['poor'] & technical_condition['very_poor'] & operational_condition['very_low'], consequence['immediate_replacement'])
rule_27 = ctrl.Rule(hydraulic_performance['poor'] & technical_condition['very_poor'] & operational_condition['low'], consequence['immediate_replacement'])
rule_28 = ctrl.Rule(hydraulic_performance['poor'] & technical_condition['very_poor'] & operational_condition['moderate'], consequence['immediate_replacement'])
rule_29 = ctrl.Rule(hydraulic_performance['poor'] & technical_condition['very_poor'] & operational_condition['high'], consequence['immediate_replacement'])
rule_30 = ctrl.Rule(hydraulic_performance['poor'] & technical_condition['very_poor'] & operational_condition['very_high'], consequence['immediate_replacement'])
rule_31 = ctrl.Rule(hydraulic_performance['poor'] & technical_condition['poor'] & operational_condition['very_low'], consequence['immediate_replacement'])
rule_32 = ctrl.Rule(hydraulic_performance['poor'] & technical_condition['poor'] & operational_condition['low'], consequence['immediate_replacement'])
rule_33 = ctrl.Rule(hydraulic_performance['poor'] & technical_condition['poor'] & operational_condition['moderate'], consequence['routine_maintenance'])
rule_34 = ctrl.Rule(hydraulic_performance['poor'] & technical_condition['poor'] & operational_condition['high'], consequence['routine_maintenance'])
rule_35 = ctrl.Rule(hydraulic_performance['poor'] & technical_condition['poor'] & operational_condition['very_high'], consequence['routine_maintenance'])
rule_36 = ctrl.Rule(hydraulic_performance['poor'] & technical_condition['fair'] & operational_condition['very_low'], consequence['routine_maintenance'])
rule_37 = ctrl.Rule(hydraulic_performance['poor'] & technical_condition['fair'] & operational_condition['low'], consequence['routine_maintenance'])
rule_38 = ctrl.Rule(hydraulic_performance['poor'] & technical_condition['fair'] & operational_condition['moderate'], consequence['routine_maintenance'])
rule_39 = ctrl.Rule(hydraulic_performance['poor'] & technical_condition['fair'] & operational_condition['high'], consequence['routine_maintenance'])
rule_40 = ctrl.Rule(hydraulic_performance['poor'] & technical_condition['fair'] & operational_condition['very_high'], consequence['routine_maintenance'])
rule_41 = ctrl.Rule(hydraulic_performance['poor'] & technical_condition['good'] & operational_condition['very_low'], consequence['routine_maintenance'])
rule_42 = ctrl.Rule(hydraulic_performance['poor'] & technical_condition['good'] & operational_condition['low'], consequence['routine_maintenance'])
rule_43 = ctrl.Rule(hydraulic_performance['poor'] & technical_condition['good'] & operational_condition['moderate'], consequence['routine_maintenance'])
rule_44 = ctrl.Rule(hydraulic_performance['poor'] & technical_condition['good'] & operational_condition['high'], consequence['routine_maintenance'])
rule_45 = ctrl.Rule(hydraulic_performance['poor'] & technical_condition['good'] & operational_condition['very_high'], consequence['routine_maintenance'])
rule_46 = ctrl.Rule(hydraulic_performance['poor'] & technical_condition['excellent'] & operational_condition['very_low'], consequence['routine_maintenance'])
rule_47 = ctrl.Rule(hydraulic_performance['poor'] & technical_condition['excellent'] & operational_condition['low'], consequence['routine_maintenance'])
rule_48 = ctrl.Rule(hydraulic_performance['poor'] & technical_condition['excellent'] & operational_condition['moderate'], consequence['routine_maintenance'])
rule_49 = ctrl.Rule(hydraulic_performance['poor'] & technical_condition['excellent'] & operational_condition['high'], consequence['routine_maintenance'])
rule_50 = ctrl.Rule(hydraulic_performance['poor'] & technical_condition['excellent'] & operational_condition['very_high'], consequence['routine_maintenance'])

rule_51 = ctrl.Rule(hydraulic_performance['fair'] & technical_condition['very_poor'] & operational_condition['very_low'], consequence['immediate_replacement'])
rule_52 = ctrl.Rule(hydraulic_performance['fair'] & technical_condition['very_poor'] & operational_condition['low'], consequence['immediate_replacement'])
rule_53 = ctrl.Rule(hydraulic_performance['fair'] & technical_condition['very_poor'] & operational_condition['moderate'], consequence['immediate_replacement'])
rule_54 = ctrl.Rule(hydraulic_performance['fair'] & technical_condition['very_poor'] & operational_condition['high'], consequence['immediate_replacement'])
rule_55 = ctrl.Rule(hydraulic_performance['fair'] & technical_condition['very_poor'] & operational_condition['very_high'], consequence['immediate_replacement'])
rule_56 = ctrl.Rule(hydraulic_performance['fair'] & technical_condition['poor'] & operational_condition['very_low'], consequence['immediate_replacement'])
rule_57 = ctrl.Rule(hydraulic_performance['fair'] & technical_condition['poor'] & operational_condition['low'], consequence['immediate_replacement'])
rule_58 = ctrl.Rule(hydraulic_performance['fair'] & technical_condition['poor'] & operational_condition['moderate'], consequence['immediate_replacement'])
rule_59 = ctrl.Rule(hydraulic_performance['fair'] & technical_condition['poor'] & operational_condition['high'], consequence['routine_maintenance'])
rule_60 = ctrl.Rule(hydraulic_performance['fair'] & technical_condition['poor'] & operational_condition['very_high'], consequence['routine_maintenance'])
rule_61 = ctrl.Rule(hydraulic_performance['fair'] & technical_condition['fair'] & operational_condition['very_low'], consequence['routine_maintenance'])
rule_62 = ctrl.Rule(hydraulic_performance['fair'] & technical_condition['fair'] & operational_condition['low'], consequence['immediate_replacement'])
rule_63 = ctrl.Rule(hydraulic_performance['fair'] & technical_condition['fair'] & operational_condition['moderate'], consequence['immediate_replacement'])
rule_64 = ctrl.Rule(hydraulic_performance['fair'] & technical_condition['fair'] & operational_condition['high'], consequence['routine_maintenance'])
rule_65 = ctrl.Rule(hydraulic_performance['fair'] & technical_condition['fair'] & operational_condition['very_high'], consequence['routine_maintenance'])
rule_66 = ctrl.Rule(hydraulic_performance['fair'] & technical_condition['good'] & operational_condition['very_low'], consequence['immediate_replacement'])
rule_67 = ctrl.Rule(hydraulic_performance['fair'] & technical_condition['good'] & operational_condition['low'], consequence['immediate_replacement'])
rule_68 = ctrl.Rule(hydraulic_performance['fair'] & technical_condition['good'] & operational_condition['moderate'], consequence['routine_maintenance'])
rule_69 = ctrl.Rule(hydraulic_performance['fair'] & technical_condition['good'] & operational_condition['high'], consequence['monitoring_only'])
rule_70 = ctrl.Rule(hydraulic_performance['fair'] & technical_condition['good'] & operational_condition['very_high'], consequence['monitoring_only'])
rule_71 = ctrl.Rule(hydraulic_performance['fair'] & technical_condition['excellent'] & operational_condition['very_low'], consequence['immediate_replacement'])
rule_72 = ctrl.Rule(hydraulic_performance['fair'] & technical_condition['excellent'] & operational_condition['low'], consequence['immediate_replacement'])
rule_73 = ctrl.Rule(hydraulic_performance['fair'] & technical_condition['excellent'] & operational_condition['moderate'], consequence['monitoring_only'])
rule_74 = ctrl.Rule(hydraulic_performance['fair'] & technical_condition['excellent'] & operational_condition['high'], consequence['monitoring_only'])
rule_75 = ctrl.Rule(hydraulic_performance['fair'] & technical_condition['excellent'] & operational_condition['very_high'], consequence['monitoring_only'])

rule_76 = ctrl.Rule(hydraulic_performance['good'] & technical_condition['very_poor'] & operational_condition['very_low'], consequence['immediate_replacement'])
rule_77 = ctrl.Rule(hydraulic_performance['good'] & technical_condition['very_poor'] & operational_condition['low'], consequence['immediate_replacement'])
rule_78 = ctrl.Rule(hydraulic_performance['good'] & technical_condition['very_poor'] & operational_condition['moderate'], consequence['immediate_replacement'])
rule_79 = ctrl.Rule(hydraulic_performance['good'] & technical_condition['very_poor'] & operational_condition['high'], consequence['immediate_replacement'])
rule_80 = ctrl.Rule(hydraulic_performance['good'] & technical_condition['very_poor'] & operational_condition['very_high'], consequence['immediate_replacement'])
rule_81 = ctrl.Rule(hydraulic_performance['good'] & technical_condition['poor'] & operational_condition['very_low'], consequence['routine_maintenance'])
rule_82 = ctrl.Rule(hydraulic_performance['good'] & technical_condition['poor'] & operational_condition['low'], consequence['routine_maintenance'])
rule_83 = ctrl.Rule(hydraulic_performance['good'] & technical_condition['poor'] & operational_condition['moderate'], consequence['routine_maintenance'])
rule_84 = ctrl.Rule(hydraulic_performance['good'] & technical_condition['poor'] & operational_condition['high'], consequence['monitoring_only'])
rule_85 = ctrl.Rule(hydraulic_performance['good'] & technical_condition['poor'] & operational_condition['very_high'], consequence['monitoring_only'])
rule_86 = ctrl.Rule(hydraulic_performance['good'] & technical_condition['fair'] & operational_condition['very_low'], consequence['monitoring_only'])
rule_87 = ctrl.Rule(hydraulic_performance['good'] & technical_condition['fair'] & operational_condition['low'], consequence['monitoring_only'])
rule_88 = ctrl.Rule(hydraulic_performance['good'] & technical_condition['fair'] & operational_condition['moderate'], consequence['monitoring_only'])
rule_89 = ctrl.Rule(hydraulic_performance['good'] & technical_condition['fair'] & operational_condition['high'], consequence['monitoring_only'])
rule_90 = ctrl.Rule(hydraulic_performance['good'] & technical_condition['fair'] & operational_condition['very_high'], consequence['monitoring_only'])
rule_91 = ctrl.Rule(hydraulic_performance['good'] & technical_condition['good'] & operational_condition['very_low'], consequence['monitoring_only'])
rule_92 = ctrl.Rule(hydraulic_performance['good'] & technical_condition['good'] & operational_condition['low'], consequence['monitoring_only'])
rule_93 = ctrl.Rule(hydraulic_performance['good'] & technical_condition['good'] & operational_condition['moderate'], consequence['monitoring_only'])
rule_94 = ctrl.Rule(hydraulic_performance['good'] & technical_condition['good'] & operational_condition['high'], consequence['monitoring_only'])
rule_95 = ctrl.Rule(hydraulic_performance['good'] & technical_condition['good'] & operational_condition['very_high'], consequence['monitoring_only'])
rule_96 = ctrl.Rule(hydraulic_performance['good'] & technical_condition['excellent'] & operational_condition['very_low'], consequence['monitoring_only'])
rule_97 = ctrl.Rule(hydraulic_performance['good'] & technical_condition['excellent'] & operational_condition['low'], consequence['monitoring_only'])
rule_98 = ctrl.Rule(hydraulic_performance['good'] & technical_condition['excellent'] & operational_condition['moderate'], consequence['monitoring_only'])
rule_99 = ctrl.Rule(hydraulic_performance['good'] & technical_condition['excellent'] & operational_condition['high'], consequence['no_action'])
rule_100 = ctrl.Rule(hydraulic_performance['good'] & technical_condition['excellent'] & operational_condition['very_high'], consequence['no_action'])

rule_101 = ctrl.Rule(hydraulic_performance['excellent'] & technical_condition['very_poor'] & operational_condition['very_low'], consequence['immediate_replacement'])
rule_102 = ctrl.Rule(hydraulic_performance['excellent'] & technical_condition['very_poor'] & operational_condition['low'], consequence['immediate_replacement'])
rule_103 = ctrl.Rule(hydraulic_performance['excellent'] & technical_condition['very_poor'] & operational_condition['moderate'], consequence['immediate_replacement'])
rule_104 = ctrl.Rule(hydraulic_performance['excellent'] & technical_condition['very_poor'] & operational_condition['high'], consequence['immediate_replacement'])
rule_105 = ctrl.Rule(hydraulic_performance['excellent'] & technical_condition['very_poor'] & operational_condition['very_high'], consequence['immediate_replacement'])
rule_106 = ctrl.Rule(hydraulic_performance['excellent'] & technical_condition['poor'] & operational_condition['very_low'], consequence['monitoring_only'])
rule_107 = ctrl.Rule(hydraulic_performance['excellent'] & technical_condition['poor'] & operational_condition['low'], consequence['monitoring_only'])
rule_108 = ctrl.Rule(hydraulic_performance['excellent'] & technical_condition['poor'] & operational_condition['moderate'], consequence['monitoring_only'])
rule_109 = ctrl.Rule(hydraulic_performance['excellent'] & technical_condition['poor'] & operational_condition['high'], consequence['monitoring_only'])
rule_110 = ctrl.Rule(hydraulic_performance['excellent'] & technical_condition['poor'] & operational_condition['very_high'], consequence['monitoring_only'])
rule_111 = ctrl.Rule(hydraulic_performance['excellent'] & technical_condition['fair'] & operational_condition['very_low'], consequence['monitoring_only'])
rule_112 = ctrl.Rule(hydraulic_performance['excellent'] & technical_condition['fair'] & operational_condition['low'], consequence['monitoring_only'])
rule_113 = ctrl.Rule(hydraulic_performance['excellent'] & technical_condition['fair'] & operational_condition['moderate'], consequence['monitoring_only'])
rule_114 = ctrl.Rule(hydraulic_performance['excellent'] & technical_condition['fair'] & operational_condition['high'], consequence['monitoring_only'])
rule_115 = ctrl.Rule(hydraulic_performance['excellent'] & technical_condition['fair'] & operational_condition['very_high'], consequence['monitoring_only'])
rule_116 = ctrl.Rule(hydraulic_performance['excellent'] & technical_condition['good'] & operational_condition['very_low'], consequence['monitoring_only'])
rule_117 = ctrl.Rule(hydraulic_performance['excellent'] & technical_condition['good'] & operational_condition['low'], consequence['monitoring_only'])
rule_118 = ctrl.Rule(hydraulic_performance['excellent'] & technical_condition['good'] & operational_condition['moderate'], consequence['monitoring_only'])
rule_119 = ctrl.Rule(hydraulic_performance['excellent'] & technical_condition['good'] & operational_condition['high'], consequence['no_action'])
rule_120 = ctrl.Rule(hydraulic_performance['excellent'] & technical_condition['good'] & operational_condition['very_high'], consequence['no_action'])
rule_121 = ctrl.Rule(hydraulic_performance['excellent'] & technical_condition['excellent'] & operational_condition['very_low'], consequence['no_action'])
rule_122 = ctrl.Rule(hydraulic_performance['excellent'] & technical_condition['excellent'] & operational_condition['low'], consequence['no_action'])
rule_123 = ctrl.Rule(hydraulic_performance['excellent'] & technical_condition['excellent'] & operational_condition['moderate'], consequence['no_action'])
rule_124 = ctrl.Rule(hydraulic_performance['excellent'] & technical_condition['excellent'] & operational_condition['high'], consequence['no_action'])
rule_125 = ctrl.Rule(hydraulic_performance['excellent'] & technical_condition['excellent'] & operational_condition['very_high'], consequence['no_action'])

# Control system
sewer_control_system = ctrl.ControlSystem([
    rule_1, rule_2, rule_3, rule_4, rule_5,
    rule_6, rule_7, rule_8, rule_9, rule_10,
    rule_11, rule_12, rule_13, rule_14, rule_15,
    rule_16, rule_17, rule_18, rule_19, rule_20,
    rule_21, rule_22, rule_23, rule_24, rule_25,

    rule_26, rule_27, rule_28, rule_29, rule_30,
    rule_31, rule_32, rule_33, rule_34, rule_35,
    rule_36, rule_37, rule_38, rule_39, rule_40,
    rule_41, rule_42, rule_43, rule_44, rule_45,
    rule_46, rule_47, rule_48, rule_49, rule_50,

    rule_51, rule_52, rule_53, rule_54, rule_55,
    rule_56, rule_57, rule_58, rule_59, rule_60,
    rule_61, rule_62, rule_63, rule_64, rule_65,
    rule_66, rule_67, rule_68, rule_69, rule_70,
    rule_71, rule_72, rule_73, rule_74, rule_75,

    rule_76, rule_77, rule_78, rule_79, rule_80,
    rule_81, rule_82, rule_83, rule_84, rule_85,
    rule_86, rule_87, rule_88, rule_89, rule_90,
    rule_91, rule_92, rule_93, rule_94, rule_95,
    rule_96, rule_97, rule_98, rule_99, rule_100,

    rule_101, rule_102, rule_103, rule_104, rule_105,
    rule_106, rule_107, rule_108, rule_109, rule_110,
    rule_111, rule_112, rule_113, rule_114, rule_115,
    rule_116, rule_117, rule_118, rule_119, rule_120,
    rule_121, rule_122, rule_123, rule_124, rule_125
])
# Simulation instance
sewer_simulation = ctrl.ControlSystemSimulation(sewer_control_system)

def get_consequence_label(result_value):
    universe = consequence.universe
    membership_values = {}
    
    for label in consequence.terms:
        membership = fuzz.interp_membership(
            universe, 
            consequence[label].mf, 
            result_value
        )
        membership_values[label] = membership
    return max(membership_values, key=membership_values.get)

def compute_cons(hp, tc, oc):
    sewer_simulation.input['hydraulic_performance'] = hp
    sewer_simulation.input['technical_condition'] = tc
    sewer_simulation.input['operational_condition'] = oc
    sewer_simulation.compute()
    return sewer_simulation.output['consequence']
