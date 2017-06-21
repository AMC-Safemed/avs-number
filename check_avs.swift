import Cocoa

func canonize (avs_number: String) -> String {
    return avs_number.replacingOccurrences(of: ".", with: "")
}

func is_valid_avs_number (avs_number: String) -> Bool {
    let canonized = canonize(avs_number: avs_number)
    var total = 0
    var nb = 0
    for (index, char) in canonized.characters.enumerated() {
        nb = Int(String(char))!
        if index % 2 != 0 {
            nb *= 3
        }
        
        total += nb
    }
    
    let actual_key = nb
    var expected_key = 0
    
    total -= actual_key
    
    if total % 10 != 0 {
        let round_ten_up = (total/10)*10 + 10
        expected_key = round_ten_up - total
    }
    
    return expected_key == actual_key
}

let example = "756.1234.5678.97"
let is_valid = is_valid_avs_number(avs_number:example)