# Project 2/3 Before PU - GC Content Calculator
# PU-CET 2027 Aspirant - Drop Year 2026

def gc_content(dna):
    dna = dna.upper()
    g = dna.count('G')
    c = dna.count('C')
    gc_percent = ((g + c) / len(dna)) * 100
    print(f"DNA: {dna}")
    print(f"GC Content: {gc_percent:.2f}%")
    print(f"G: {g}, C: {c}")
    if gc_percent > 60:
        print("High GC = More Stable")

gc_content("ATGCGCGCGATATATGC")
gc_content("GGCCGGCCGG")
