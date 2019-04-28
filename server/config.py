TEAM_NUMBERS = {
    "Bushwhackers": 1,
    "FAUST": 2,
    "[SPbCTF] LC↯BC": 3,
    "VoidHack": 4,
    "Shadow Servants": 5,
    "B3vil (ex. 0x1dea)": 6,
    "Lights Out": 7,
    "bacaro_tour": 8,
    "saarsec": 9,
    "ОМСКИЙ АНДЕГРАУНД И КУБОК ПЕТУХА": 10,
    "Kamneezhka": 11,
    "Corrupted Reflection": 12,
    "kks_wund3rw4ffl3_team": 13,
    "[SPbCTF] fargate": 14,
    "ZenHack": 15,
    "SwissMadeSecurity": 16,
    "SiBears": 17,
    "Honeypot": 18,
    "SharLike": 19,
    "Omaviat": 20,
    "10.60.21": 21,
    "10.60.22": 22,
    "Pixels": 23,
    "ENOFLAG": 24,
    "Gleitkommafreunde Bonn": 25,
    "[SPbCTF] Kappa": 26,
    "Tower of Hanoi": 27,
    "STT": 28,
}
TEAMS = {'#{}: {}'.format(number, name): '10.60.{}.1'.format(number)
         for name, number in TEAM_NUMBERS.items()}
# unknown_numbers = set(range(1, 30)) - set(TEAM_NUMBERS.values())
# for number in unknown_numbers:
    # TEAMS['#{}: <UNK>'.format(number)] = '10.60.{}.1'.format(number)

CONFIG = {
    # Don't forget to remove the old database (flags.sqlite) before each competition.

    # The clients will run sploits on TEAMS and
    # fetch FLAG_FORMAT from sploits' stdout.
    'TEAMS': TEAMS,
    'FLAG_FORMAT': r'[A-Z0-9]{31}=',

    # This configures how and where to submit flags.
    # The protocol must be a module in protocols/ directory.
    # RuCTF(E) and VolgaCTF checksystems are supported out-of-the-box.

    'SYSTEM_PROTOCOL': 'ructf_tcp',
    'SYSTEM_HOST': '10.10.10.10',
    'SYSTEM_PORT': 31337,

    # 'SYSTEM_PROTOCOL': 'ructf_http',
    # 'SYSTEM_URL': 'http://monitor.ructfe.org/flags',
    # 'SYSTEM_TOKEN': 'your_secret_token',

    # 'SYSTEM_PROTOCOL': 'volgactf',
    # 'SYSTEM_HOST': '127.0.0.1',

    # The server will submit not more than SUBMIT_FLAG_LIMIT flags
    # every SUBMIT_PERIOD seconds. Flags received more than
    # FLAG_LIFETIME seconds ago will be skipped.
    'SUBMIT_FLAG_LIMIT': 50,
    'SUBMIT_PERIOD': 5,
    'FLAG_LIFETIME': 10 * 60,

    # Password for the web interface. This key will be excluded from config
    # before sending it to farm clients.
    'SERVER_PASSWORD': '1234',

    # Use authorization for API requests
    'ENABLE_API_AUTH': False,
    'API_TOKEN': '00000000000000000000'
}
