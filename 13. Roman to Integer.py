def romanToInt(s: str) -> int:
    result = 0
    keys_dic = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }
    keys_dic_comp = {
        'IV': 4,
        'IX': 9,
        'XL': 40,
        'XC': 90,
        'CD': 400,
        'CM': 900
    }

    symbol = 0
    while symbol < len(s):
        print(symbol)
        print(s[symbol])

        if s[symbol] == 'I' or s[symbol] == 'X' or s[symbol] == 'C':
            if s[symbol:symbol + 2] in keys_dic_comp.keys():
                result += keys_dic_comp[s[symbol:symbol + 2]]
                symbol += 2
            else:
                result += keys_dic[s[symbol]]
                symbol += 1

        else:
            result += keys_dic[s[symbol]]
            symbol += 1

    return result


if __name__ == '__main__':
    # print(romanToInt("MCMXCIV"))
    print(romanToInt('MCDLXXVI'))