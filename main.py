#https://github.com/sankeer-28
from confusables import Confusables
import itertools

def show_menu():
    print("1 - Show menu")
    print("2 - Input a letter and output all characters similar to that letter")
    print("3 - Input an English word and output all possible letters of that word")
    print("4 - Input an English word and print out all the varieties of that word")
    print("5 - Exit the program")

def list_letter_varieties(letter, confusables):
    if letter in confusables.confusables_dict:
        print(letter + ": " + "".join(confusables.confusables_dict[letter]))
    else:
        print(letter + ": No similar characters found")

def list_word_varieties(word, confusables):
    pattern = confusables.confusables_regex(word)
    print(pattern)

def print_word_varieties(word, confusables):
    char_lists = []
    for char in word:
        if char in confusables.confusables_dict:
            char_lists.append([char] + confusables.confusables_dict[char])
        else:
            char_lists.append([char])
    for combination in itertools.product(*char_lists):
        print(''.join(combination))

confusables = Confusables('https://www.unicode.org/Public/draft/security/confusables.txt')

#added the characters from Lingo-jam
confusables.confusables_dict['a'].extend(['🅰', 'ɐ', '∀', 'ɒ', 'ą', 'Ⱥ', 'ᴀ', 'Ⓐ', 'ⓐ', 'α', 'Ａ', 'ａ', 'ᗩ', '卂', 'Δ', 'ค', 'α', 'ά', 'Ã', '𝔞', '𝓪', '𝒶', '𝓐', '𝐀', '𝐚', '𝔸', '𝕒', 'ᵃ'])
confusables.confusables_dict['b'].extend(['🅱', 'q', 'ᙠ', 'd', 'ᙠ', 'ҍ', 'β', 'ʙ', 'Ⓑ', 'ⓑ', 'в', 'Ｂ', '乃', 'ｂ', 'ᗷ', 'β', '๒', 'в', 'в', 'β', '𝔟', '  𝓫', '𝒷', '𝓑', '𝐁', '𝐛', '𝔹', '𝕓', 'ᵇ'])
confusables.confusables_dict['c'].extend(['🅲', 'ɔ', 'Ɔ', 'ɔ', 'Ɔ', 'ç', '↻', 'ᴄ', 'Ⓒ', 'ⓒ', '匚', '¢', 'Ｃ', 'ｃ', 'ᑕ', 'Ć', 'ς', 'c', 'ς', 'Č', '℃', '� ', '𝓬', '𝒸', '𝓒', '𝐂', '𝐜', 'ℂ', '𝕔', 'ᶜ'])
confusables.confusables_dict['d'].extend(['🅳', 'p', 'ᗡ', 'ᗡ', 'ժ', 'Ꭰ', 'ᴅ', 'Ⓓ', 'ⓓ', '∂', 'Ｄ', 'ｄ', 'ᗪ', 'Đ', '๔', '∂', 'đ', 'Ď', '𝔡', '𝓭', '𝒹',     '𝓓', '𝐃', 'ᗪ', '𝐝', '𝔻', '𝕕', 'ᵈ'])
confusables.confusables_dict['e'].extend(['🅴', 'ǝ', 'Ǝ', 'ɘ', 'Ǝ', 'ҽ', 'Ɛ', 'ᴇ', 'Ⓔ', '乇', 'ⓔ', 'є', 'Ｅ', 'ｅ', 'ᗴ', '€ ', 'є', 'ε', 'έ', 'Ẹ', '𝔢', '𝒆', '𝑒', '𝓔', '𝐄', '𝐞', '𝔼', '𝕖', 'ᵉ'])
confusables.confusables_dict['f'].extend(['🅵', 'ɟ', 'Ⅎ', 'Ꮈ', 'ꟻ', 'ƒ', 'Ƒ', 'ꜰ', 'Ⓕ', 'ⓕ', 'ƒ', 'Ｆ', 'ｆ', '千', 'ᖴ', 'ℱ', 'Ŧ', 'ғ', 'ғ', 'Ƒ', '𝔣', '  𝒇', '𝒻', '𝓕', '𝐅', '𝐟', '𝔽', '𝕗', 'ᶠ'])
confusables.confusables_dict['g'].extend(['🅶', 'ɓ', '⅁', 'ǫ', 'Ꭾ', 'ց', 'Ɠ', 'ɢ', 'Ⓖ', 'ⓖ', 'ق', 'g', 'Ｇ', 'ｇ', 'Ǥ', 'Ꮆ', 'ﻮ', 'g', 'ģ', 'Ğ', '𝔤', '�  ', '𝑔', '𝓖', '𝐆', '𝐠', '𝔾', '𝕘', 'ᵍ', 'Ꮆ'])
confusables.confusables_dict['h'].extend(['🅷', 'ɥ', 'ʜ', 'հ', 'Ƕ', 'ʜ', 'Ⓗ', '卄', 'ⓗ', 'н', 'Ｈ', 'ｈ', 'ᕼ', 'Ħ', 'ђ', 'н', 'ħ', 'Ĥ', '𝔥', '𝓱', '𝒽', '𝓗', '𝐇', '𝐡', 'ℍ', '𝕙', 'ʰ'])
confusables.confusables_dict['i'].extend(['🅸', 'ı', 'ì', 'į', 'ɪ', 'Ⓘ', 'ⓘ', 'ι', 'Ｉ', 'ｉ', 'Ꭵ', '丨', 'Ɨ', 'เ', 'ι', 'ί', 'Į', '𝔦', '𝓲', '𝒾', '𝓘'     , '𝐈', '𝐢', '𝕀', '𝕚', 'ᶤ'])
confusables.confusables_dict['j'].extend(['🅹', 'ɾ', 'ſ', 'ꞁ', 'Ⴑ', 'ʝ', 'ل', 'ᴊ', 'Ⓙ', 'ⓙ', 'נ', 'Ｊ', 'ڶ', 'ｊ', 'ᒎ', 'Ĵ', 'ן', 'נ', 'ј', 'Ĵ', '𝔧', '�  ', '𝒿', '𝓙', '𝐉', '𝐣', '𝕁', '𝕛', 'ʲ'])
confusables.confusables_dict['k'].extend(['🅺', 'ʞ', '⋊', 'ʞ', '⋊', 'ҟ', 'Ҡ', 'ᴋ', 'Ⓚ', 'ⓚ', 'к', 'Ｋ', 'ｋ', 'ᛕ', 'Ҝ', 'к', 'к', 'ķ', 'Ќ', '𝔨', '𝓴', '   𝓀', '𝓚', '𝐊', '𝐤', '𝕂', '𝕜', 'ᵏ', 'Ҝ'])
confusables.confusables_dict['l'].extend(['🅻', 'l', '˥', '|', '⅃', 'Ӏ', 'Ꝉ', 'ʟ', 'Ⓛ', 'ⓛ', 'ℓ', 'ㄥ', 'Ｌ', 'ｌ', 'ᒪ', 'Ł', 'l', 'ℓ', 'Ļ', 'Ĺ', '𝔩', '  𝓵', '𝓁', '𝓛', '𝐋', '𝐥', '𝕃', '𝕝', 'ˡ'])
confusables.confusables_dict['m'].extend(['🅼', 'ɯ', 'W', 'ʍ', 'Ɱ', 'ᴍ', 'Ⓜ', 'ⓜ', 'м', 'Ｍ', 'ｍ', 'ᗰ', 'Μ', '๓', 'м', 'м', 'ϻ', '𝔪', '𝓶', '𝓂', '𝓜',     '𝐌', '𝐦', '𝕄', '𝕞', 'ᵐ', '爪'])
confusables.confusables_dict['n'].extend(['V2', '🅽', 'u', 'ᴎ', 'Ͷ', 'ղ', 'ហ', 'ɴ', 'Ⓝ', '几', 'ⓝ', 'η', 'Ｎ', 'ｎ', 'ᑎ', 'Ň', 'ภ', 'η' , 'ή', 'Ň', '𝔫', '𝓷', '𝓃', '𝓝', '𝐍', '𝐧', 'ℕ', '𝕟', 'ᶰ'])
confusables.confusables_dict['o'].extend(['🅾', 'օ', 'ට', 'ᴏ', 'Ⓞ', 'ㄖ', 'ⓞ', 'σ', 'Ｏ', 'ｏ', 'ᗝ', 'Ø', '๏', 'σ', 'ό', 'Ỗ', '𝔬', '𝓸', '𝑜', '𝓞', '𝐎      ', '𝐨', '𝕆', '𝕠', 'ᵒ'])
confusables.confusables_dict['p'].extend(['🅿', 'Ԁ', 'q', 'ꟼ', 'ք', 'φ', 'ᴘ', 'Ⓟ', 'ⓟ', 'ρ', 'Ｐ', 'ｐ', '卩', 'ᑭ', 'Ƥ', 'ק', 'ρ', 'ρ', 'Ƥ', '𝔭', '𝓹',    '𝓅', '𝓟', '𝐏', '𝐩', 'ℙ', '𝕡', 'ᵖ'])
confusables.confusables_dict['q'].extend(['🆀', 'Ό', 'Ọ', 'զ', 'Ҩ', 'Q', 'Ⓠ', 'ⓠ', 'q', 'Ｑ', 'ｑ', 'Ɋ', 'Ω', 'ợ', 'q', 'q', 'Ǫ', '𝔮', '𝓺', '𝓆', '𝓠',     '𝐐', '𝐪', 'ℚ', '𝕢', 'ᵠ'])
confusables.confusables_dict['r'].extend(['🆁', 'ɹ', 'ᴚ', 'ɿ', 'Я', 'ɾ', 'འ', 'ʀ', 'Ⓡ', 'ⓡ', 'я', '尺', 'Ｒ', 'ｒ', 'ᖇ', 'Ř', 'г', 'я', 'ŕ', 'Ř', '𝔯', '  𝓻', '𝓇', '𝓡', '𝐑', '𝐫', 'ℝ', '𝕣', 'ʳ'])
confusables.confusables_dict['s'].extend([ '🆂', 'ꙅ', 'Ꙅ', 'ʂ', 'Ϛ', 'ꜱ', 'Ⓢ', 'ⓢ', 'ѕ', 'Ｓ', '丂', 'ｓ', 'ᔕ', 'Ş', 'ร', 's', 'ş', 'Ŝ', '𝔰', '𝓼', '𝓈', '𝓢', '𝐒', '𝐬', '𝕊', '𝕤', 'ˢ'])
confusables.confusables_dict['t'].extend(['🆃', 'ʇ', '⊥', 'ƚ', 'է', 'Ͳ', 'ᴛ', 'Ⓣ', 'ⓣ', 'т', 'Ｔ', 'ｔ', '丅', 'Ŧ', 't', 'т', 'ţ', 'Ť',  '𝔱', '𝓽', '𝓉', '𝓣', '𝐓', '𝐭', '𝕋', '𝕥', 'ᵗ'])
confusables.confusables_dict['u'].extend(['🆄', '∩', 'մ', 'Ա', 'ᴜ', 'Ⓤ', 'ⓤ', 'υ', 'Ｕ', 'ｕ', 'ᑌ', 'Ữ', 'ย', 'υ', 'ù', 'Ǘ', '𝔲', '𝓾', '𝓊', '𝓤', '𝐔'      , '𝐮', '𝕌', '𝕦', 'ᵘ'])
confusables.confusables_dict['v'].extend(['🆅', 'ʌ', 'Λ', 'ѵ', 'Ỽ', 'ᴠ', 'Ⓥ', 'ⓥ', 'ν', 'Ｖ', 'ｖ', 'ᐯ', 'V', 'ש', 'v', 'ν', 'Ѷ', '𝔳', '𝓿', '𝓋', '𝓥',     '𝐕', '𝐯', '𝕍', '𝕧', 'ᵛ'])
confusables.confusables_dict['w'].extend(['🆆', 'ʍ', 'ա', 'చ', 'ᴡ', 'Ⓦ', 'ⓦ', 'ω', 'Ｗ', 'ｗ', 'ᗯ', 'Ŵ', 'ฬ', 'ω', 'ώ', 'Ŵ', '𝔴', '𝔀', '𝓌', '𝓦', '𝐖'      , '𝐰', '𝕎', '𝕨', 'ʷ', '山'])
confusables.confusables_dict['x'].extend(['🆇', '×', 'ჯ', 'x', 'Ⓧ', 'ⓧ', 'χ', 'Ｘ', '乂', 'ｘ', '᙭', 'Ж', 'א', 'x', 'x', 'Ж', '𝔵', '𝔁', '𝓍', '𝓧', '𝐗      ', '𝐱', '𝕏', '𝕩', 'ˣ'])
confusables.confusables_dict['y'].extend(['🆈', 'ʎ', '⅄', 'ʏ', 'վ', 'Ӌ', 'ʏ', 'Ⓨ', 'ㄚ', 'ⓨ', 'у', 'Ｙ', 'ｙ', 'Ƴ', '¥', 'ץ', 'ү', 'ч', 'Ў', '𝔶', '𝔂',    '𝓎', '𝓨', '𝐘', '𝐲', '𝕐', '𝕪', 'ʸ'])
confusables.confusables_dict['z'].extend(['🆉', 'ƹ', 'Ƹ', 'Հ', 'ɀ', 'ᴢ', 'Ⓩ', 'ⓩ', 'z', '乙', 'Ｚ', 'ｚ', 'Ƶ', 'Ž', 'z', 'z', 'ž', 'Ż', '𝔷', '𝔃', '𝓏',    '𝓩', '𝐙', '𝐳', 'ℤ', '𝕫', 'ᶻ'])



show_menu()
while True:
    choice = input("Enter your choice: ")
    if choice == '1':
        show_menu()
    elif choice == '2':
        letter = input("Enter a letter: ")
        list_letter_varieties(letter, confusables)
    elif choice == '3':
        word = input("Enter an English word: ")
        list_word_varieties(word, confusables)
    elif choice == '4':
        word = input("Enter an English word: ")
        print_word_varieties(word, confusables)
    elif choice == '5':
        break
