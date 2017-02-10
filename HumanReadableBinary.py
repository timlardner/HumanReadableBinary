def convert(file_name,binary):
    with open(file_name,'w') as file:
        for byte in binary:
            for bit in bitfield(byte):
                file.write(str(bit))
    
def bitfield(n):
    return [1 if digit=='1' else 0 for digit in bin(n)[2:]]


        
    



