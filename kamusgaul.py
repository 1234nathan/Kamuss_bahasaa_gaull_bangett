meme_dict = {
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
            "ROLF" : "Tanggan terhadap lelucon",
            "SHEESH" : "sedikit ketidaksetujuan",
            "CREEPY" : "menakutkan, tidak menyenangkan",
            "AGGRO" : "untuk menjadi agresih/marah",
            }
while True :            
    word = input("Ketik kata yang tidak Kamu mengerti (gunakan huruf kapital semua!): ")

    if word in meme_dict.keys():
        print(meme_dict[word])
        break
    else:
        print("invalid")
