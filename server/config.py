TEAM_NAMES = ['!@NoTeamHere', '529', 'SiBears', '!@NoTeamHere', 'cyberwehr', 'HgbSec', 'CInsects', 'saarsec', 'NUSecLab', 'BlueSheep', 'Xain', '0x01d5', 'thirumalaivasan', 'ωhατεvεr', 'qwerty', 'KATE', 'Corrupted_Lights', 'Gabana', 'M.I.S.T.', 'Lab104', 'SpontaneousSecurity', 'Kaeiel', 'WE_0WN_Y0U', 'gorogoroumaru', '0xDECA', 'ENOFLAG', 'GleitkommafreundeBonn', 'Life', 'xmun0x', 'R3dCr3sc3nt', 'NoPwnIntended', 'n0tyr3x', 'gnuDucks', '3xp10it5', 'TheGrandPew', 'Ne0Lux-C1Ph3r', 'stankc', 'void_pointer', 'Nerds_of_Mayhem', 'Recursion_Fairies', 'pwnthem0le', 'CondomOnFire', 'Shadow_Servants', 'Jaitej', 'Bob', '!@NoTeamHere', 'MLPWN', 'robon', 'fargate', 'Бямбадалай', '!@NoTeamHere', 'Goutham', 'P@Ge2mE', 'page2me', 'Cyb3rZ0n3', 'GEMPA', '0FA', 'the4960', 'kks', 'hddev', 'Team7', 'KonungarnirFróðleikar', 'acdwas', '23783702', 'sploit00n', 'Blue_Team_Bangladesh', 'Aquin', '!@NoTeamHere', 'UTSAHackers', 'Effractarius_Electronicus', 'noraneco', 'Kirill', '0x6e6f6f62', 'chiduc97', '!@NoTeamHere', 'SU', 'webcult', '2O2L2H', 'Lurkrul', '!@NoTeamHere', 'Xan0er', 'blueship', 'room2042', 'aiQG', 'SIGFLAG', 'Noname179', 'Joel', 'onotch', 'warlock_rootx', '!@NoTeamHere', 'definitively_a_trowaway_account', 'dcua', 'Slotleet', 'ismail', 'dixie_flatline', 'flagbot', 'Defenit', 'RedCadets', 'Akshansh', 'kandoi', '!@NoTeamHere', 'Schrodinger', 'iohex', 'Pizza', 'SPbCTF@Kappa', 'top30kret', 'Iam9r00t', 't1', 'NIS', 'CTBUAP', 'FluxFingers', 'STT', 'Kamneezhka', 'UrlNo', 'bolgai4', 'p4wnWAT', 'swt02026', 'FlagBusters', 'z3d', 'badfirmware', 'ppppppp', 'd4rkr00t', 'BTeam', '7hetSEC', 'Salvat0re', 't3kk1', 'LosFuzzys', '!@NoTeamHere', 'ld3k0fv', 'CRC', '!@NoTeamHere', 'Kfftfuftur', 'Domeki', 'Bushwhackers', 'R3C01L', 'he11o', 'iwnltoday', 'ObjectNotFound', 'epist', 'EvilBunnyWrote', 'N0p3', 'Shellphish', 'alexost66', 'upbhack', 'BinaryBears', 'XSHELL', 'pattern', 'LaPWN', 'deAthstr_kE', 'PwnaSonic', 'sto4mbr3ak3rs', 'k3rn3l_dw3ll3rs', 'npc', 'SharLike', 'tmpMe', 'Byt3Scr4pp3rs', 'MvtinaPwn', 'CCUG', 'VoidHack', '!@NoTeamHere', 'ZenHack', 'awawa', 'glua.team', 'ErPaciocco.Smhacko', 'FrauMeow', 'SinHack', 'fzhshzh', 'SquidwardTheBeast', 'Corrman', 'Antiver', '晴雯晴雯', 'Team_M', 'Vasilisa', 'bi0s', 'NULLKrypt3rs', '!@NoTeamHere', 'Switzerland12Points', '4n0nym0u5_dr34m3r', 'BSOD', 'Sonexteen', 'bmtd', 'Dc1ph3R', 'Gh0stSh3ll', 'ETH4ck3rs', 'SPbCTF', '!@NoTeamHere', 'Beater', 'cokomel', 'fkillrra', '10sec', 'PeaceMaker', '!@NoTeamHere', 'TheRomanXpl0it', 'NaN-ny', 'Lancet', 'Omaviat', 'NothernCoalition', 'born2scan', 'mitsu', 'crackerz', 'wunderleth', 'haiclover', 'bhajjaka', 'Jeffrey', 'roborobo', 'redCat', 'WFTC', 'HooKReS', 'hj', 'Tony', 'CTD_Elite', 'lovelace3777', 'OpenToAll', '!@NoTeamHere', 'ALLES', 'perfect_blue', 'SUID', 'andser612345', 'noob_team_0', 'rec0de', 'Socks312', 'zeroonepixel', 'cotds', 'phildragonbleu', 'N3wbi3_Kor', 'Ch0p5t1ck', 'asd', '!@NoTeamHere', 'regreet', 'ByteForc3', 'NextLineSolo', 'a80215', 'Djavaa', 'gh0sh', 'l33tn00b', 'CodeByO', 'kishalon', '!@NoTeamHere', 'Lorse', '!@NoTeamHere', 'HTsP', 'd071ik3', '!@NoTeamHere', 'SGJL', 'fr0g2s', 'qw3709', 'Neo', 'Giuseppe', 'SCSHT']

TEAM_NUMBERS = {
    name: i
    for i, name in enumerate(TEAM_NAMES, start=1)
    if not name.startswith('!@')
}
TEAMS = {'#{}: {}'.format(number, name): '10.65.{}.1'.format(number)
         for name, number in TEAM_NUMBERS.items()}
# unknown_numbers = set(range(1, 30)) - set(TEAM_NUMBERS.values())
# for number in unknown_numbers:
    # TEAMS['#{}: <UNK>'.format(number)] = '10.60.{}.1'.format(number)

CONFIG = {
    # Don't forget to remove the old database (flags.sqlite) before each competition.

    # The clients will run sploits on TEAMS and
    # fetch FLAG_FORMAT from sploits' stdout.
    'TEAMS': TEAMS,
    'FLAG_FORMAT': r'FAUST_[A-Za-z0-9/\+]{32}',

    # This configures how and where to submit flags.
    # The protocol must be a module in protocols/ directory.
    # RuCTF(E) and VolgaCTF checksystems are supported out-of-the-box.

    'SYSTEM_PROTOCOL': 'ructf_tcp',
    'SYSTEM_HOST': 'submission.faustctf.net',
    'SYSTEM_PORT': 666,

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
