mkdir ./generated
python main.py --with cr3.txt cr2.txt cr1.txt --vs 20 > generated/spp1of3.scad
python main.py --with cr4.txt cr4.txt --vs 20 > generated/spp2of3.scad
python main.py --with cr3.txt cr2.txt cr1.txt --vs 20 > generated/spp3of3.scad
python main.py --with cr1.txt cr2.txt cr3.txt cr4.txt cr4.txt cr3.txt cr2.txt cr1.txt --vs 20 > generated/blocky_sphere.scad
