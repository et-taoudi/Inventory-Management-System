def calculate_checksum(box_ids):
    count_two = 0  # Counter for IDs with exactly two repeated letters
    count_three = 0  # Counter for IDs with exactly three repeated letters
    repeated_letters_two = []  # List to store letters repeated twice
    repeated_letters_three = []  # List to store letters repeated three times

    for box_id in box_ids:
        letter_count = {}  # Dictionary to store the count of each letter in the box ID

        # Count the occurrences of each letter in the box ID
        for letter in box_id:
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1

        # Check if there are any letters with exactly two or three occurrences
        for letter, count in letter_count.items():
            if count == 2 and letter not in repeated_letters_two:
                count_two += 1
                repeated_letters_two.append(letter)
            elif count == 3 and letter not in repeated_letters_three:
                count_three += 1
                repeated_letters_three.append(letter)

    # Calculate the checksum by multiplying the counts
    checksum = count_two * count_three

    return checksum, count_two, count_three


# Example
box_ids = ["abcdefne", "bababc", "abbcde", "abcccd", "aabcdd", "abcdee", "ababab"]
checksum = calculate_checksum(box_ids)
print(f"The checksum is: {checksum[0]}")
print(f"The letters repeated 2 times : {checksum[1]}")
print(f"The letters repeated 3 times: {checksum[2]}")

# Example with puzzle input
box_ids = ["krdmtuqjmwfoevnadixyclzspv", "yrdmtuqjiwfoevnabfxyclzsph", "kqjvtuqjgwfoevnabixyclzsph", "krdmtuqjgwjoevnaolxyclzsph", "krdmtnqjgwfoevnabiiyxlzsph", "lrymtuqjgwhoevnabixyclzsph", "krdmguqjgwfoevnabixkclzsah","krdmtuqjgwfoevnibinyclzdph","krdmtucjgwfoevnabhxyclzspv","krdmtuqjgwfoevtabixyulzsuh","krdmtuqqgwfoevnabixdblzsph","krdmtuqjawfsevnabiyyclzsph","krdmtuqjgwfoevnabzxccldsph","krdmtcqegwfhevnabixyclzsph","krdmtuqjgwforvnaxixycgzsph","krdmtuqjgwfoqvnaxixyclzskh","krdmtutjgwfoevyajixyclzsph","krdmtuqmgwfoevnabixycxzspc","krdptuqjgwhoevkabixyclzsph","krdttuqjhwfoevnabixyclzspa","krdmtuqjgwfoevnabibyhnzsph",
           "krdmtuqjywfoevntbidyclzsph","krdmtojdgwfoevnabixyclzsph","krdmtuqjgpfuevnauixyclzsph","krdmtoqjgwfrevjabixyclzsph","krdmtuqjgwfoyvndbixyclzyph","krdmtxqjgwfomvnayixyclzsph","crdmtuqjgwfoevnabixyoxzsph","krdmtpqjgwfdevnabixycqzsph","krdmtuqjgwfoevuabfxsclzsph","krdmtuqjgwfoevnybixycdzskh","krdmtusjgwfoevnabixxclzdph",
           "krdmtuqjgwfoevnaboxyglzjph","zrdmtuqjgrfoevnalixyclzsph","krdmtuqjclfoevnabixyclzsih","kqdmtlqjgwfoevnabtxyclzsph","krdmtuqggwpoevnabixyclzlph","krdmtuqjgwfobwnrbixyclzsph","krdmtuqjgwfoevwabkxycnzsph","kldmtuqjgwfogvyabixyclzsph","krdmtuqvgwfoevnabixtcrzsph","krdmtuqjgwroevnabixyrlzspw","krdmtuqjgjfoevnabixyelzrph","krdmtuqjgffoevnaaixyclzspa","krdmtuqjgwfoevxabifywlzsph",
           "krdmtuqjgwfoevlabixycrzsrh","krdmtuqjgwfpevnabixocqzsph","krdmtuqjgwfoevdabixycnhsph","krdmtmqjgwfoevnajixyclvsph","krdmtuqjjvfoevnabgxyclzsph","krzmtuqjgwfoevnabioyckzsph","kodmtwqjgwfoevnabieyclzsph","ehdmthqjgwfoevnabixyclzsph","krdmtuqjxwioevnabixyclbsph","grdmkutjgwfoevnabixyclzsph","krdutuqjgwfoebnabixaclzsph","krdmtuqjgwfoebnabixyclcjph",
           "krdmteqjgwfoevnlbixycizsph","krdmtegjgwhoevnabixyclzsph","krdmtuqjgwfdrvnabixbclzsph","krdmtuqjgyfoevidbixyclzsph","krdmtubjawfoevnabixyclzuph","krdmtuqjgwfoavjabixyclzssh","krdmtuqjgwfoeonabixyclzsvo","vrdmtuqjgwffevnabixpclzsph","krdmtuqonwfoevnabixycfzsph","krdmtumjgwfpevnubixyclzsph","krdmtutjgwfoevnaciyyclzsph","krdrtuqjgwfoevnwbixyglzsph","krdmtuqjgwfoevbabixyclesdh","krdmtuqcgwfoevnabixyqdzsph",
           "krdmtuqjgwfogvnabrxycezsph","krdmujqkgwfoevnabixyclzsph","krdmtuqjgtooevnabixyclzzph","jrdntuqjgwfoevnabixyclrsph","krdmtuqjgzfoevkebixyclzsph","krdmtuqjgwfosvnaeixyclztph","krdmtuqjgwfoevzabixydlzaph",
            "krdmtuqzgwfoavnabiqyclzsph",
            "krdmtuqvgwfoevnabixycwzspv",
            "krdmvuqjgwteevnabixyclzsph",
            "krdmtujjgwfoevgybixyclzsph",
            "kydmtuqjgwfoeunacixyclzsph",
            "krdmtuqjgifoqvnabicyclzsph",
            "krnltiqjgwfoevnabixyclzsph",
            "krdmtuqjgwfoevnabhxyclzsgi",
            "kfdmtuqjnwfowvnabixyclzsph",
            "kmdmtuljgwfoevnabixycvzsph",
            "krdmtxqjgwaoevvabixyclzsph",
            "kramduqjgwfoevnabixyclzwph",
            "krdutuqjgwfoennabixyclziph",
            "krdmvuqfgwfoevnacixyclzsph",
            "krdmtuqogwfoevnabmvyclzsph",
            "krdmfuqjgwfoyvnabixyclzseh",
            "krdmtuqjgweoelnabixyclzspd",
            "krdmtumjgwfoevnabixyclzypo",
            "krdmtuqjgkfoevhabixyclzsqh",
            "kjdmtuqjgwfoevgabixyclzsah",
            "krdmtuqjgwfoevnlbixyclzsbw",
            "mrdmtxqjgwfoevnabgxyclzsph",
            "krdmtuqpgwfoevnhbixycltsph",
            "krdmtuqjgwfmqvnabixyclzslh",
            "krqmtuqogwfoevnaqixyclzsph",
            "krdmtusjggfoevnabicyclzsph",
            "krcmtuljgwfoevlabixyclzsph",
            "krdmtuojgwfoeknabixyclzsrh",
            "krdmtuqjtwfoevnabiypclzsph",
            "krvmtupjgwfoevnabixycldsph",
            "krdmtuxjgwfoevaabxxyclzsph",
            "krdmtvqlgwfoehnabixyclzsph",
            "wrdmtuqjgwfoevnabixyclzdpy",
            "krdatuqlgwfoevnabixyclzsjh",
            "krdmtuqjgwfoevpabkxyclzsjh",
            "krdmtuqjgwqvsvnabixyclzsph",
            "krdmtwqjgwfoevnobixyclzspm",
            "krdmtuqjgssoevnabixyclgsph",
            "krdmtuqjgwfoevnafixyclzbpp",
            "krdmtuqjowfoevxabiuyclzsph",
            "krdmtuqrgwfoevntbixyclzspu",
            "krdmtucjgwfoevnabixcnlzsph",
            "krddtuojgwfoevnabixyclzzph",
            "krdmtuqjgwuoevnabiqycldsph",
            "kpdmpuqjgwfoevnabixyclzslh",
            "krdmtuqjgwfoewnabixyzxzsph",
            "krdmtuejswfoevhabixyclzsph",
            "krdmtuqggwfoevntbikyclzsph",
            "krdmtuqjgwfoevnabixydlhnph",
            "krdmtcqjglfoevnaxixyclzsph",
            "krumyuqjgwfoevnrbixyclzsph",
            "kgdmmuqjgwooevnabixyclzsph",
            "krdmteqjgwfqevwabixyclzsph",
            "krdmfuqjgwfpevnabixyclzspq",
            "erdmtycjgwfoevnabixyclzsph",
            "krdmcuqjgwfoevnabixjglzsph",
            "krdmtuqjgtfoeunabixiclzsph",
            "krdmtuqjgwfoevmqbixyclzspu",
            "krlmtuqjvwfoevnabikyclzsph",
            "krdotuqjgwfoevnagrxyclzsph",
            "krdmtuqbgwfoefnabixyclasph",
            "kwdmtuqjgwfosjnabixyclzsph",
            "kydmtuqjgwfoevcabixycezsph",
            "crdmtuqjgwloevnabixkclzsph",
            "krimtuqhgwfoevnbbixyclzsph",
            "krdmjuqagwfoevnabicyclzsph",
            "krdmtuqdgzfoevnabixydlzsph",
            "krdmtuqjgwwoevnaqixyclzspf",
            "krdmtuqjgwfoevnabdxyzvzsph",
            "krdmtuqjgwaofvnabixyclzsnh",
            "krdmturjgwfmevnabixyclzspn",
            "krdmvuqjgwboevnabixyolzsph",
            "krdmtuqjgwfomvnabijyclzspx",
            "bedmtuqjgwfoevnabixyslzsph",
            "krdmtenjgwfoevnabixyclzsqh",
            "krdmtuqugwfoevnabixpcdzsph",
            "krdmtuqjgiloevnabrxyclzsph",
            "krdmtupjcwfoevnabixyclwsph",
            "kremtuqjgwfoevnabixyyjzsph",
            "krdmtuqjgwnoovnabixyclzshh",
            "qrdmtuqjgwfoevnabixyciasph",
            "krdituqjgbfoevnagixyclzsph",
            "krdmnoqjgwfoqvnabixyclzsph",
            "krdmtuqegwfoevhkbixyclzsph",
            "krdmkucjgwfoevnabixnclzsph",
            "krdmtuqbnwpoevnabixyclzsph",
            "krdmttqjgwfoevnabixyclbspz",
            "srdmtubjgwfrevnabixyclzsph",
            "krdmruqjzwfoevnabixyclesph",
            "ardmtuqfgwwoevnabixyclzsph",
            "yrumtuqjgwhoevnabixyclzsph",
            "rrdmtuqjgwfoevnabsxycwzsph",
            "krpmtuqjgwfoevdabixyclzzph",
            "krdmuuqjgwfoevnabixyclriph",
            "krdmtuqjgwfobvnabixyvgzsph",
            "krdmbuujgwfoevnabixycczsph",
            "krhmtuwjgwfoeqnabixyclzsph",
            "krdwtuqjgwfoevnkbixyclzzph",
            "krdmtuqjgwkoeqnabixyvlzsph",
            "kadmtuqjgwfoednabcxyclzsph",
            "krdmtyqqgwfoevnabizyclzsph",
            "krdmtuqjgnfoevnabiyycmzsph",
            "krdmtuqjcwfouvnabixyclznph",
            "krdmtuqjjwfcevnqbixyclzsph",
            "krdmtuqfgbfoevgabixyclzsph",
            "kkdmtuqjgwfoevnapixyclzsth",
            "nrdmtuqjgwtoevnakixyclzsph",
            "krdmtuqjglfoevlabixdclzsph",
            "zrdmtuqjgwfoevndbixbclzsph",
            "krdmeuqjgwfoeenabixyclrsph",
            "krdmoaqjzwfoevnabixyclzsph",
            "krsmtuqjgwfoevnwbixyclzsfh",
            "kadmtuqjgwfoqdnabixyclzsph",
            "krsmtuqjgofoevnabixkclzsph",
            "krdmtuqjdwfoevnibixdclzsph",
            "mrdmtuqjgwfouvnabixyclzfph",
            "trdmtlqjgwfoevnabixyclzjph",
            "trdmyuqjgwfozvnabixyclzsph",
            "krdmtiqjgwroevnabixyclzspk",
            "erdmtutjgwftevnabixyclzsph",
            "krdwyuqjgwfoevnaaixyclzsph",
            "krdmthqbgwfoevnabixyclksph",
            "krdmttqjgwfoivnabixyclvsph",
            "krdmtuqjgwfoefnabixyflgsph",
            "khdmtuqjgwfoevnajixyvlzsph",
            "krdmtuqvgwfoevnasixyclzspt",
            "krdmtuqjgkwogvnabixyclzsph",
            "krdmtuqjgwfoevnaboxpglzjph",
            "kadmtuqjgwfoxvnabixyclziph",
            "krdmtuqjfwfoevnabaxycbzsph",
            "krdjtuqjgwfoevnabiryhlzsph",
            "krdvtuqjgpfoevnabcxyclzsph",
            "brdmtuqjgwfoevnafixyqlzsph",
            "krdmtuqjgwfoevnavixxcllsph",
            "krdhtuqjkwfoevfabixyclzsph",
            "krdmtuqjgjfoevnawixyclzsuh",
            "krddtuqjgwfoeqnabiwyclzsph",
            "krhmtuqjgwfnevnabinyclzsph",
            "kedmtuqjgzfmevnabixyclzsph",
            "qrdmtuqjgwfoevntbixyclzxph",
            "krdmtuqsgwfoevnabixvclzrph",
            "scdmtuqjgwfoevnabixtclzsph",
            "krymtuqjgjfolvnabixyclzsph",
            "krdmtuqjgwfkevnablxyclzskh",
            "krymtuqjswfoevnabixyclzvph",
            "krdmtuqjhwfoevnabixycwzspd",
            "krdmtuxjgwfoevnabyxyclzzph",
            "krdmtlqjgwfovvnabilyclzsph",
            "krdmtuqjgwfoevnaaijcclzsph",
            "krdatrqjgwfokvnabixyclzsph",
            "krdmtuqjgwfoevnaxifyclzkph",
            "krddtuqjgwfoevnabixccozsph",
            "krdmtuqngwfoevnabiyycxzsph",
            "krdmtumdgwfoevnqbixyclzsph",
            "krdmtuqjgwfoevnabixyxlmsch",
            "krdmtudzgwfoevnabixtclzsph",
            "krdmtuqjgwfoevnpbixyclhspl",
            "krdmtqqjgwjoevnabexyclzsph",
            "kydmtuqzgwfoevnabixyclwsph",
            "krdmeucjgwqoevnabixyclzsph",
            "krdmtuqjghfoevjabixyclzspp",
            "krdmtuqjgjfwevnabixyclzskh",
            "krdmkuhjgwfoevnabipyclzsph",
            "krdytuqjgwfoevnabibyclztph",
            "krdmtuqjgwfpevnabisyzlzsph",
            "kmdmtgqjgwfsevnabixyclzsph",
            "krdmtuqjgsfoevnabijyclzszh",
            "krdmtuqjgwfoevnabivyclzuuh",
            "krdstuqjgrfoevnabixyclzspu",
            "jrdmtuqjgwfotvnabixyclzspj",
            "krdmrumjgwfoevnabixeclzsph",
            "krpmtusjgwfoevnabioyclzsph"]
checksum = calculate_checksum(box_ids)
print(f"The checksum is: {checksum[0]}")
print(f"The letters repeated 2 times : {checksum[1]}")
print(f"The letters repeated 3 times: {checksum[2]}")

