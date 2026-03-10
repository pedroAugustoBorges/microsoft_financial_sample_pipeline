
def validate_empty(data):
    valid = []
    invalid = []
    
    
    for d in data:
        
        is_valid = True
        
        for item in d.values():
            print(item)
            if not item:
                invalid.append({"row" : 6, "reason" : "empty field"})
                is_valid = False
                break
            
        if is_valid:
            valid.append(d)
    
    return (valid, invalid)
                        
        
def test_empty(s):
    if not s:
        print('string is empty')
    else:
        print('print is not empty')
        

test_empty('d')