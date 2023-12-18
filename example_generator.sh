mkdir ./generated
python main.py --with cr3.txt cr2.txt cr1.txt --vs 20 > generated/spp1of3.scad
python main.py --with cr4.txt cr4.txt --vs 20 > generated/spp2of3.scad
python main.py --with cr3.txt cr2.txt cr1.txt --vs 20 > generated/spp3of3.scad
python main.py --with cr1.txt cr2.txt cr3.txt cr4.txt cr4.txt cr3.txt cr2.txt cr1.txt --vs 20 > generated/blocky_sphere.scad

python main.py --with hcc1.txt hcc2.txt hcc3.txt hcc4.txt hcc5.txt hcc6.txt hcc7.txt hcc8.txt --vs 50 > generated/hollow_blocky_cube.scad

python main.py --with hhc1.txt hhc2.txt hhc3.txt hhc4.txt hhc5.txt hhc6.txt hhc7.txt hhc8.txt --vs 50 > generated/hollow_healer_cube.scad
