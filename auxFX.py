import random


def replaceBySmallCaps(text):
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
               "v", "w", "x", "y", "z"]
    smallCaps = {
        "a": "ᴀ",
        "b": "ʙ",
        "c": "ᴄ",
        "d": "ᴅ",
        "e": "ᴇ",
        "f": "ғ",
        "g": "ɢ",
        "h": "ʜ",
        "i": "ɪ",
        "j": "ᴊ",
        "k": "ᴋ",
        "l": "ʟ",
        "m": "ᴍ",
        "n": "ɴ",
        "o": "ᴏ",
        "p": "ᴘ",
        "q": "ǫ",
        "r": "ʀ",
        "s": "s",
        "t": "ᴛ",
        "u": "ᴜ",
        "v": "ᴠ",
        "w": "ᴡ",
        "x": "x",
        "y": "ʏ",
        "z": "ᴢ"
    }
    out = ""
    for char in text.lower():
        if char in letters:
            out = out + smallCaps.get(char)
        else:
            out = out + char
    return out


def truncate(_target, length):
    out = ""
    i = 0
    target = str(_target)

    for char in target:
        i += 1
        out = out + char
        if char == ".":
            break

    k = 0
    for j in range(length):
        out = out + target[i + k]
        k += 1

    return float(out + "0")


def checkPass(text):
    password = (
        b"a4 df 87 fe bf b0 40 b9 8b e8 91 dd 34 c2 66 5e f1 7c 72 46 65 2a 38 64 55 98 e0 e6 81 69 5a 89 ec 36 "
        b"b4 29 0c 80 8d 9e 6d 57 ea 92 1f 11 02 f3 ce c5 82 71 a9 35 1d b3 8a cd 3b 21 61 cc 8b 25")
    return hash(text) == password


def nameReportChannel(reportedPlayer):
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
               "v", "w", "x", "y", "z"]
    firstLetter = ""
    out = ""
    i = 0

    for char in reportedPlayer:
        if char.lower() in letters:
            firstLetter = char.upper()
            break
        i += 1

    return f"{firstLetter}→{reportedPlayer}"


def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)


class log:
    info = "info"
    warn = "warn"
    error = "error"
    debug = "debug"


def consoleLog(logType, text):
    def colored(r, g, b, txt):
        return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, txt)

    colors = dict(info=(92, 150, 44), warn=(190, 170, 12), error=(240, 67, 94), debug=(160, 137, 255))
    log = dict(info="[INFO    ]", warn="[WARNING ]", error="[ERROR   ]", debug="[DEBUG   ]")

    out = [colors.get(logType)[0], colors.get(logType)[1], colors.get(logType)[2], text]
    print(colored(out[0], out[1], out[2], f"{log.get(logType)} {out[3]}"))


def fileLog(logType, text, logFile="log.txt"):
    log = dict(info="[INFO   ]", warn="[WARNING]", error="[ERROR  ]", debug="[DEBUG  ]")

    out = [log.get(logType), text]

    with open(logFile, "a") as saveLog:
        saveLog.write(f"{out[0]} {out[1]}")
        saveLog.close()


def returnStatusMenu(_target, sender):
    target = ""

    if len(_target) > 16:
        for i in range(16):
            target = target + _target[i]

    else:
        target = _target

    targetNameLength = len(target)
    characterLack = 16 - targetNameLength

    if characterLack < 16:
        charBefore = characterLack // 2
        charAfter = (characterLack // 2) + (characterLack % 2)

    else:
        charBefore = charAfter = 0

    _headerMid = [(" " * charBefore) + target + (" " * charAfter)]

    headerMid = ""

    for i in range(len(_headerMid)):
        headerMid = headerMid + _headerMid[i]

    header = f"`===============-  {headerMid}  -===============`"
    footer = f"`===============- PalaBlacklist 2024 -===============`"

    OUT = \
        f"||.||\n\n{header}\n\n**ATTENTION:** Cette fonctionnalité est pour le moment toujours en développement, et peut être modifié, améliorée, ou supprimée à tout moment. Des erreurs peuvent et vont arriver.\n\n{footer}"

    return OUT


def generateString(seed, length):
    out = ""

    for i in range(length):
        out = out + random.choice(seed)

    return out


# ======================================================================================================================
#                             This file is a part of TechnoSpirit's LunaFur bot. If you want
#                             to modify it, or do your own version, but you are taking parts
#                             of this version, please leave this text at the end of the file
#                                                           ---
#                             Thank you for using LunaFur and I hope it satisfied your needs
#
# ======================================================================================================================
