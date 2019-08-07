drones = [
    {
        'id': '3DR-IRIS',
        'wingtype': 'rotary',
        'takeoffweight': 1.282,
        'speedmax': 0,
        'endurancemax': 15,
        'endurancemaxspeed': 0,
        'endurancemaxhover': 0,
        'rangemax': 0,
        'rangemaxspeed': 0,
        'temperaturemin,': -10,
        'waterproof': 'no',
        'rotorquantity': 4,
        'rotordiameter': 0.254,
        'cruisespeed': 0.0,
        'payload': 0.0,
        'length': 0.280,
        'width': 0.140,
        'height': 0.100,
        'battery': {
            'batterytype': 'LiPo',
            'batterycapacity': 3500,
            'batteryvoltage': 11.1,
            'batterycells': 3,
            'batterymass': 0.262
        }
    },
    {
        'id': '3DR-Solo',
        'wingtype': 'rotary',
        'rotorquantity': 4,
        'rotordiameter': 0.254,
        'takeoffweight': 1.5,
        'endurancemax': 25,
        'altitudemax': 100,
        'payloadmax': 0.5,
        'speedmax': 25.5,
        'cruise_speed': 2.5,
        'windspeedmax': 11,
        'temperaturemin': 0,
        'temperaturemax': 45,
        'humiditymax': 85,
        'props': '10x4.5',
        'battery': {
            'batterytype': 'LiPo',
            'batterycapacity': 5200,
            'batteryvoltage': 14.8,
            'batterymass': 0.5            
        }
    },
    {
        'id': 'aerovironment-Puma3AE',
        'wingtype': 'fixed',
        'endurancemax': 150,
        'takeoffweight': 6.8,
        'span': 2.8,
        'altitudemax': 152,
        'battery': {
            'batterytype': 'LE'            
        }
    },
    {
        'id': 'aeryon-skyrangerR70',
        'wingtype': 'rotary',
        'rotorquantity': 4,
        'speedmax': 13.89,
        'endurancemax': 35,
        'max_payload': 2.0,
        'altitudemax': 4572,
        'windspeedmax': 19.44,
        'temperaturemin': -20,
        'temperaturemax': 50,
        'waterproof': 'yes',
        'takeoffweight': 4.5,
        'battery': {
            'num_batteries': 4            
        }
    },
    {
        'id': 'asctec-Falcon8',
        'wingtype': 'rotary',
        'max_takeoffweight': 2.3,
        'max_payload': 0.8,
        'endurancemax': 22,
        'speedmax': 15,
        'windspeedmax': 12,
        'temperaturemin': -5,
        'temperaturemax': 35,
        'rotorquantity': 8,
        'rotordiameter': 0.2,
        'battery': {
            'batterytype': 'LiPo',
            'batterycells': 3,
            'batterycapacity': 6250,
            'batterymass': 0.426            
        }
    },
    {
        'id': 'dji-Mavic2',
        'wingtype': 'rotary',
        'diagonal': 0.354,
        'takeoffweight': 0.907,
        'speedmax': 20,
        'altitudemax': 6000,
        'endurancemax': 31,
        'endurancemaxspeed': 6.944,
        'endurancemaxhover': 29,
        'rangemax': 18000,
        'rangemaxspeed': 13.889,
        'tiltanglemax': 35,
        'temperaturemin': -10,
        # 'endurancemax': 40,
        'chargerpowerrating': 60,
        'battery': {
            'batterytype': 'LiPo',
            'batterycapacity': 3850,
            'batteryvoltage': 15.4,
            'batterycells': 4,
            'batteryenergy': 59.29,
            'batterymass': 0.297
        },
        'waterproof': 'no',
        'windspeedmax': 10.8,
        'batteryrechargetime': 90,
        'rotorquantity': 4,
        'rotordiameter': 0.2,
        'cruisespeed': 6.94,
        'payload': 0.0,
        'length': 0.322,
        'width': 0.242,
        'height': 0.084
    },
    {
        'id': 'dji-Phantom4RTK',
        'wingtype': 'rotary',
        'diagonal': 0.350,
        'takeoffweight': 1.391,
        'altitudemax': 6000,
        'speedmax': 16.0934,
        'temperaturemin': 0,
        'temperaturemax': 40,
        'endurancemax': 30,
        'props': '9450s Quick Release',
        'rotorquantity': 4,
        'battery': {
            'batterytype': 'LiPo',
            'batterymass': 0.468,
            'batterycells': 4,
            'batteryvoltage': 15.2,
            'batterycapacity': 5870,
            'batteryenergy': 89.2,            
            'batteryrechargetime': 60
        }
    },
    {
        'id': 'freefly-alta8',
        'wingtype': 'rotary',
        'rotorquantity': 8,
        'diagonal': 1.325,
        'takeoffweightmax': 18.1,
        'empty_weight': 6.2,
        'payloadmax': 9.1,
        'specific_power': 145,
        'props': '18x6_Folding',
        'motor_max_power_continuous': 350,
        'motor_max_power_peak': 950,
        'temperaturemin': -20,
        'temperaturemax': 45,
        'thrust_ratio_at_max_takeoffweight': '1.85:1',
        'battery': {
            'batterycells': 6,
            'batteryvoltage': 22.2,
            'batterycapacity': 10000,
            'batterytype': 'LiPo',
            'num_batteries': 2,
            'numbatteriesconnection': 'parallel'    
        }
    },
    {
        'id': 'precisionhawk-FireFLY6Pro',
        'wingtype': 'fixed',
        'span': 1.524,
        'takeoffweight': 4.5,
        'endurancemax': 59,
        'speedmax' : 31,
        'max_payload': 0.7,
        'cruise_speed': 18,
        'VTOL': 'yes',
        'waterproof' : 'yes',
        'battery': {
        'batterytype': 'LiHV'            
        }
    },
    {
        'id': 'senseFly-ebeeX',
        'wingtype': 'fixed',
        'span': 1.16,
        'takeoffweight': 1.4,
        'speedmax': 30,
        'endurancemax': 90,
        'windspeedmax': 12.8,
        'VTOL': 'no',
        'battery': {
            'batterytype': 'LiPo',
            'batterycapacity': 4900,
            'batteryvoltage': 14.8,
            'batterycells': 4,
            'batterymass': 0.4,
            'batteryrechargetime': 40     
        }
    },
    {
        'id': 'yuneec-TyphoonHPlus',
        'wingtype': 'rotary',
        'diagonal': 0.520,
        'rotorquantity': 6,
        'takeoffweight': 1.645,
        'endurancemax': 28,
        'speedmax': 13.4112,
        'altitudemax': 500,
        'temperaturemin': 0,
        'temperaturemax': 40,
        'battery': {
            'batterytype': 'LiPo',
            'batterycells': 4,
            'batteryvoltage': 14.8,
            'batterycapacity': 5400    
        }
    }
]

conversions = {
    'speedmax': 1.0,
    'altitudemax': 1.0,
    'endurancemax': 60.0,
    'chargerpowerrating': 1.0,
    'batterycapacity': 3.6,
    'batteryvoltage': 1.0,
    'batteryenergy': 3600.0,
    'batterymass': 1.0,
    'batteryrechargetime': 60.0,
    'endurancemaxhover': 60.0,
    'windspeedmax': 1.0,
    'rotordiameter': 1.0
}