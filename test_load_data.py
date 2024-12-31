# ECOR 1042 Lab 4 - team submission

#import check module here
import check

#import load_data module here
import load_data

# Update "" with your the name of the active members of the team
__author__ = "RILEY HANNA, CAROLINE TWELVES, ADAM LOFARO, MARYAM ALSHAWAFI"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T098"

#==========================================#

# Place test_return_list function here 
def test_return_list():

    check.equal(load_data.machine_vendor_list('machine-test.csv', 'amdahl'), [{'Model': '470v/7', 'MYCT': 29, 'MMIN': 8000, 'MMAX': 32000, 'CACH': 32, 'PRP': 269, 'ERP': 253}, {'Model': '470v/7a', 'MYCT': 29, 'MMIN': 8000, 'MMAX': 32000, 'CACH': 32, 'PRP': 220, 'ERP': 253}, {'Model': '470v/7b', 'MYCT': 29, 'MMIN': 8000, 'MMAX': 32000, 'CACH': 32, 'PRP': 172, 'ERP': 253}, {'Model': '470v/7c', 'MYCT': 29, 'MMIN': 8000, 'MMAX': 16000, 'CACH': 32, 'PRP': 132, 'ERP': 132}, {'Model': '470v/b', 'MYCT': 26, 'MMIN': 8000, 'MMAX': 32000, 'CACH': 64, 'PRP': 318, 'ERP': 290}, {'Model': '580-5840', 'MYCT': 23, 'MMIN': 16000, 'MMAX': 32000, 'CACH': 64, 'PRP': 367, 'ERP': 381}, {'Model': '580-5840', 'MYCT': 23, 'MMIN': 16000, 'MMAX': 32000, 'CACH': 64, 'PRP': 489, 'ERP': 381}, {'Model': '580-5840', 'MYCT': 23, 'MMIN': 16000, 'MMAX': 64000, 'CACH': 64, 'PRP': 636, 'ERP': 749}, {'Model': '580-5840', 'MYCT': 23, 'MMIN': 32000, 'MMAX': 64000, 'CACH': 128, 'PRP': 1144, 'ERP': 1238}])
    check.equal(load_data.machine_vendor_list('machine-test.csv', 'iytdiytiyu'), [])
    check.equal(load_data.machine_vendor_list('machine-test.csv', '0858087'), [])

    check.equal(load_data.machine_model_list('machine-test.csv', '470v/7'), [{'Vendor': 'amdahl', 'MYCT': 29, 'MMIN': 8000, 'MMAX': 32000, 'CACH': 32, 'PRP': 269, 'ERP': 253}])
    check.equal(load_data.machine_model_list('machine-test.csv', 'iytdiytiyu'), [])
    check.equal(load_data.machine_model_list('machine-test.csv', '0858087'), [])

    check.equal(load_data.machine_cache_list('machine-test.csv', 128), [{'Vendor': 'amdahl', 'Model': '580-5840', 'MYCT': 23, 'MMIN': 32000, 'MMAX': 64000, 'PRP': 1144, 'ERP': 1238}, {'Vendor': 'burroughs', 'Model': 'b4955', 'MYCT': 110, 'MMIN': 5000, 'MMAX': 5000, 'PRP': 120, 'ERP': 124}])
    check.equal(load_data.machine_cache_list('machine-test.csv', 0), [{'Vendor': 'amdahl', 'Model': '470v/7', 'MYCT': 29, 'MMIN': 8000, 'MMAX': 32000, 'PRP': 269, 'ERP': 253}, {'Vendor': 'amdahl', 'Model': '470v/7a', 'MYCT': 29, 'MMIN': 8000, 'MMAX': 32000, 'PRP': 220, 'ERP': 253}, {'Vendor': 'amdahl', 'Model': '470v/7b', 'MYCT': 29, 'MMIN': 8000, 'MMAX': 32000, 'PRP': 172, 'ERP': 253}, {'Vendor': 'amdahl', 'Model': '470v/7c', 'MYCT': 29, 'MMIN': 8000, 'MMAX': 16000, 'PRP': 132, 'ERP': 132}, {'Vendor': 'amdahl', 'Model': '470v/b', 'MYCT': 26, 'MMIN': 8000, 'MMAX': 32000, 'PRP': 318, 'ERP': 290}, {'Vendor': 'amdahl', 'Model': '580-5840', 'MYCT': 23, 'MMIN': 16000, 'MMAX': 32000, 'PRP': 367, 'ERP': 381}, {'Vendor': 'amdahl', 'Model': '580-5840', 'MYCT': 23, 'MMIN': 16000, 'MMAX': 32000, 'PRP': 489, 'ERP': 381}, {'Vendor': 'amdahl', 'Model': '580-5840', 'MYCT': 23, 'MMIN': 16000, 'MMAX': 64000, 'PRP': 636, 'ERP': 749}, {'Vendor': 'amdahl', 'Model': '580-5840', 'MYCT': 23, 'MMIN': 32000, 'MMAX': 64000, 'PRP': 1144, 'ERP': 1238}, {'Vendor': 'apollo', 'Model': 'dn320', 'MYCT': 400, 'MMIN': 1000, 'MMAX': 3000, 'PRP': 38, 'ERP': 23}, {'Vendor': 'basf', 'Model': 'Jul-65', 'MYCT': 60, 'MMIN': 2000, 'MMAX': 8000, 'PRP': 92, 'ERP': 70}, {'Vendor': 'basf', 'Model': 'Jul-68', 'MYCT': 50, 'MMIN': 4000, 'MMAX': 16000, 'PRP': 138, 'ERP': 117}, {'Vendor': 'bti', 'Model': '5000', 'MYCT': 350, 'MMIN': 64, 'MMAX': 64, 'PRP': 10, 'ERP': 15}, {'Vendor': 'bti', 'Model': '8000', 'MYCT': 200, 'MMIN': 512, 'MMAX': 16000, 'PRP': 35, 'ERP': 64}, {'Vendor': 'burroughs', 'Model': 'b1955', 'MYCT': 167, 'MMIN': 524, 'MMAX': 2000, 'PRP': 19, 'ERP': 23}, {'Vendor': 'burroughs', 'Model': 'b2900', 'MYCT': 143, 'MMIN': 512, 'MMAX': 5000, 'PRP': 28, 'ERP': 29}, {'Vendor': 'burroughs', 'Model': 'b2925', 'MYCT': 143, 'MMIN': 1000, 'MMAX': 2000, 'PRP': 31, 'ERP': 22}, {'Vendor': 'burroughs', 'Model': 'b4955', 'MYCT': 110, 'MMIN': 5000, 'MMAX': 5000, 'PRP': 120, 'ERP': 124}, {'Vendor': 'burroughs', 'Model': 'b5900', 'MYCT': 143, 'MMIN': 1500, 'MMAX': 6300, 'PRP': 30, 'ERP': 35}, {'Vendor': 'burroughs', 'Model': 'b5920', 'MYCT': 143, 'MMIN': 3100, 'MMAX': 6200, 'PRP': 33, 'ERP': 39}, {'Vendor': 'burroughs', 'Model': 'b6900', 'MYCT': 143, 'MMIN': 2300, 'MMAX': 6200, 'PRP': 61, 'ERP': 40}, {'Vendor': 'burroughs', 'Model': 'b6925', 'MYCT': 110, 'MMIN': 3100, 'MMAX': 6200, 'PRP': 76, 'ERP': 45}])
    check.equal(load_data.machine_cache_list('machine-test.csv', 9999), [])

    check.equal(load_data.machine_prp_list('machine-test.csv', 600), [{'Vendor': 'amdahl', 'Model': '580-5840', 'MYCT': 23, 'MMIN': 16000, 'MMAX': 64000, 'CACH': 64, 'ERP': 749}, {'Vendor': 'amdahl', 'Model': '580-5840', 'MYCT': 23, 'MMIN': 32000, 'MMAX': 64000, 'CACH': 128, 'ERP': 1238}])
    check.equal(load_data.machine_prp_list('machine-test.csv', 2000), [])
    check.equal(load_data.machine_prp_list('machine-test.csv', 0), [{'Vendor': 'amdahl', 'Model': '470v/7', 'MYCT': 29, 'MMIN': 8000, 'MMAX': 32000, 'CACH': 32, 'ERP': 253}, {'Vendor': 'amdahl', 'Model': '470v/7a', 'MYCT': 29, 'MMIN': 8000, 'MMAX': 32000, 'CACH': 32, 'ERP': 253}, {'Vendor': 'amdahl', 'Model': '470v/7b', 'MYCT': 29, 'MMIN': 8000, 'MMAX': 32000, 'CACH': 32, 'ERP': 253}, {'Vendor': 'amdahl', 'Model': '470v/7c', 'MYCT': 29, 'MMIN': 8000, 'MMAX': 16000, 'CACH': 32, 'ERP': 132}, {'Vendor': 'amdahl', 'Model': '470v/b', 'MYCT': 26, 'MMIN': 8000, 'MMAX': 32000, 'CACH': 64, 'ERP': 290}, {'Vendor': 'amdahl', 'Model': '580-5840', 'MYCT': 23, 'MMIN': 16000, 'MMAX': 32000, 'CACH': 64, 'ERP': 381}, {'Vendor': 'amdahl', 'Model': '580-5840', 'MYCT': 23, 'MMIN': 16000, 'MMAX': 32000, 'CACH': 64, 'ERP': 381}, {'Vendor': 'amdahl', 'Model': '580-5840', 'MYCT': 23, 'MMIN': 16000, 'MMAX': 64000, 'CACH': 64, 'ERP': 749}, {'Vendor': 'amdahl', 'Model': '580-5840', 'MYCT': 23, 'MMIN': 32000, 'MMAX': 64000, 'CACH': 128, 'ERP': 1238}, {'Vendor': 'apollo', 'Model': 'dn320', 'MYCT': 400, 'MMIN': 1000, 'MMAX': 3000, 'CACH': 0, 'ERP': 23}, {'Vendor': 'basf', 'Model': 'Jul-65', 'MYCT': 60, 'MMIN': 2000, 'MMAX': 8000, 'CACH': 65, 'ERP': 70}, {'Vendor': 'basf', 'Model': 'Jul-68', 'MYCT': 50, 'MMIN': 4000, 'MMAX': 16000, 'CACH': 65, 'ERP': 117}, {'Vendor': 'bti', 'Model': '5000', 'MYCT': 350, 'MMIN': 64, 'MMAX': 64, 'CACH': 0, 'ERP': 15}, {'Vendor': 'bti', 'Model': '8000', 'MYCT': 200, 'MMIN': 512, 'MMAX': 16000, 'CACH': 0, 'ERP': 64}, {'Vendor': 'burroughs', 'Model': 'b1955', 'MYCT': 167, 'MMIN': 524, 'MMAX': 2000, 'CACH': 8, 'ERP': 23}, {'Vendor': 'burroughs', 'Model': 'b2900', 'MYCT': 143, 'MMIN': 512, 'MMAX': 5000, 'CACH': 0, 'ERP': 29}, {'Vendor': 'burroughs', 'Model': 'b2925', 'MYCT': 143, 'MMIN': 1000, 'MMAX': 2000, 'CACH': 0, 'ERP': 22}, {'Vendor': 'burroughs', 'Model': 'b4955', 'MYCT': 110, 'MMIN': 5000, 'MMAX': 5000, 'CACH': 142, 'ERP': 124}, {'Vendor': 'burroughs', 'Model': 'b5900', 'MYCT': 143, 'MMIN': 1500, 'MMAX': 6300, 'CACH': 0, 'ERP': 35}, {'Vendor': 'burroughs', 'Model': 'b5920', 'MYCT': 143, 'MMIN': 3100, 'MMAX': 6200, 'CACH': 0, 'ERP': 39}, {'Vendor': 'burroughs', 'Model': 'b6900', 'MYCT': 143, 'MMIN': 2300, 'MMAX': 6200, 'CACH': 0, 'ERP': 40}, {'Vendor': 'burroughs', 'Model': 'b6925', 'MYCT': 110, 'MMIN': 3100, 'MMAX': 6200, 'CACH': 0, 'ERP': 45}])

    check.equal(load_data.add_average_main_memory([{'Vendor': 'amdahl', 'Model': '470v/7', 'MYCT': 29, 'MMIN': 8000, 'MMAX': 32000, 'CACH': 32, 'PRP': 269, 'ERP': 253}]), [{'Vendor': 'amdahl', 'Model': '470v/7', 'MYCT': 29, 'MMIN': 8000, 'MMAX': 32000, 'CACH': 32, 'PRP': 269, 'ERP': 253, 'M_AVG': 20000.0}])
    check.equal(load_data.add_average_main_memory([{'Vendor': 'apollo', 'Model': 'dn320', 'MYCT': 400, 'MMIN': 1000, 'MMAX': 3000, 'CACH': 0, 'PRP': 38, 'ERP': 23}, {'Vendor': 'basf', 'Model': 'Jul-65', 'MYCT': 60, 'MMIN': 2000, 'MMAX': 8000, 'CACH': 65, 'PRP': 92, 'ERP': 70}]), [{'Vendor': 'apollo', 'Model': 'dn320', 'MYCT': 400, 'MMIN': 1000, 'MMAX': 3000, 'CACH': 0, 'PRP': 38, 'ERP': 23, 'M_AVG': 2000.0}, {'Vendor': 'basf', 'Model': 'Jul-65', 'MYCT': 60, 'MMIN': 2000, 'MMAX': 8000, 'CACH': 65, 'PRP': 92, 'ERP': 70, 'M_AVG': 5000.0}])
    check.equal(load_data.add_average_main_memory([]), ([]))

    check.equal(load_data.load_data('machine-test.csv', ('Vendor', 'apollo')), [{'Model': 'dn320', 'MYCT': 400, 'MMIN': 1000, 'MMAX': 3000, 'CACH': 0, 'PRP': 38, 'ERP': 23}])
    check.equal(load_data.load_data('machine-test.csv', ('Model', 'universe:68/37')), [])
    check.equal(load_data.load_data('machine-test.csv', ('CACH', 256)), [])
    check.equal(load_data.load_data('machine-test.csv', ('PRP', 600)), [{'Vendor': 'amdahl', 'Model': '580-5840', 'MYCT': 23, 'MMIN': 16000, 'MMAX': 64000, 'CACH': 64, 'ERP': 749}, {'Vendor': 'amdahl', 'Model': '580-5840', 'MYCT': 23, 'MMIN': 32000, 'MMAX': 64000, 'CACH': 128, 'ERP': 1238}])
    check.equal(load_data.load_data('machine-test.csv', ('ALL', 69)), [{'Vendor': 'amdahl', 'Model': '470v/7', 'MYCT': 29, 'MMIN': 8000, 'MMAX': 32000, 'CACH': 32, 'PRP': 269, 'ERP': 253}, {'Vendor': 'amdahl', 'Model': '470v/7a', 'MYCT': 29, 'MMIN': 8000, 'MMAX': 32000, 'CACH': 32, 'PRP': 220, 'ERP': 253}, {'Vendor': 'amdahl', 'Model': '470v/7b', 'MYCT': 29, 'MMIN': 8000, 'MMAX': 32000, 'CACH': 32, 'PRP': 172, 'ERP': 253}, {'Vendor': 'amdahl', 'Model': '470v/7c', 'MYCT': 29, 'MMIN': 8000, 'MMAX': 16000, 'CACH': 32, 'PRP': 132, 'ERP': 132}, {'Vendor': 'amdahl', 'Model': '470v/b', 'MYCT': 26, 'MMIN': 8000, 'MMAX': 32000, 'CACH': 64, 'PRP': 318, 'ERP': 290}, {'Vendor': 'amdahl', 'Model': '580-5840', 'MYCT': 23, 'MMIN': 16000, 'MMAX': 32000, 'CACH': 64, 'PRP': 367, 'ERP': 381}, {'Vendor': 'amdahl', 'Model': '580-5840', 'MYCT': 23, 'MMIN': 16000, 'MMAX': 32000, 'CACH': 64, 'PRP': 489, 'ERP': 381}, {'Vendor': 'amdahl', 'Model': '580-5840', 'MYCT': 23, 'MMIN': 16000, 'MMAX': 64000, 'CACH': 64, 'PRP': 636, 'ERP': 749}, {'Vendor': 'amdahl', 'Model': '580-5840', 'MYCT': 23, 'MMIN': 32000, 'MMAX': 64000, 'CACH': 128, 'PRP': 1144, 'ERP': 1238}, {'Vendor': 'apollo', 'Model': 'dn320', 'MYCT': 400, 'MMIN': 1000, 'MMAX': 3000, 'CACH': 0, 'PRP': 38, 'ERP': 23}, {'Vendor': 'basf', 'Model': 'Jul-65', 'MYCT': 60, 'MMIN': 2000, 'MMAX': 8000, 'CACH': 65, 'PRP': 92, 'ERP': 70}, {'Vendor': 'basf', 'Model': 'Jul-68', 'MYCT': 50, 'MMIN': 4000, 'MMAX': 16000, 'CACH': 65, 'PRP': 138, 'ERP': 117}, {'Vendor': 'bti', 'Model': '5000', 'MYCT': 350, 'MMIN': 64, 'MMAX': 64, 'CACH': 0, 'PRP': 10, 'ERP': 15}, {'Vendor': 'bti', 'Model': '8000', 'MYCT': 200, 'MMIN': 512, 'MMAX': 16000, 'CACH': 0, 'PRP': 35, 'ERP': 64}, {'Vendor': 'burroughs', 'Model': 'b1955', 'MYCT': 167, 'MMIN': 524, 'MMAX': 2000, 'CACH': 8, 'PRP': 19, 'ERP': 23}, {'Vendor': 'burroughs', 'Model': 'b2900', 'MYCT': 143, 'MMIN': 512, 'MMAX': 5000, 'CACH': 0, 'PRP': 28, 'ERP': 29}, {'Vendor': 'burroughs', 'Model': 'b2925', 'MYCT': 143, 'MMIN': 1000, 'MMAX': 2000, 'CACH': 0, 'PRP': 31, 'ERP': 22}, {'Vendor': 'burroughs', 'Model': 'b4955', 'MYCT': 110, 'MMIN': 5000, 'MMAX': 5000, 'CACH': 142, 'PRP': 120, 'ERP': 124}, {'Vendor': 'burroughs', 'Model': 'b5900', 'MYCT': 143, 'MMIN': 1500, 'MMAX': 6300, 'CACH': 0, 'PRP': 30, 'ERP': 35}, {'Vendor': 'burroughs', 'Model': 'b5920', 'MYCT': 143, 'MMIN': 3100, 'MMAX': 6200, 'CACH': 0, 'PRP': 33, 'ERP': 39}, {'Vendor': 'burroughs', 'Model': 'b6900', 'MYCT': 143, 'MMIN': 2300, 'MMAX': 6200, 'CACH': 0, 'PRP': 61, 'ERP': 40}, {'Vendor': 'burroughs', 'Model': 'b6925', 'MYCT': 110, 'MMIN': 3100, 'MMAX': 6200, 'CACH': 0, 'PRP': 76, 'ERP': 45}])
    check.equal(load_data.load_data('machine-test.csv', ('ALL', 0)), [{'Vendor': 'amdahl', 'Model': '470v/7', 'MYCT': 29, 'MMIN': 8000, 'MMAX': 32000, 'CACH': 32, 'PRP': 269, 'ERP': 253}, {'Vendor': 'amdahl', 'Model': '470v/7a', 'MYCT': 29, 'MMIN': 8000, 'MMAX': 32000, 'CACH': 32, 'PRP': 220, 'ERP': 253}, {'Vendor': 'amdahl', 'Model': '470v/7b', 'MYCT': 29, 'MMIN': 8000, 'MMAX': 32000, 'CACH': 32, 'PRP': 172, 'ERP': 253}, {'Vendor': 'amdahl', 'Model': '470v/7c', 'MYCT': 29, 'MMIN': 8000, 'MMAX': 16000, 'CACH': 32, 'PRP': 132, 'ERP': 132}, {'Vendor': 'amdahl', 'Model': '470v/b', 'MYCT': 26, 'MMIN': 8000, 'MMAX': 32000, 'CACH': 64, 'PRP': 318, 'ERP': 290}, {'Vendor': 'amdahl', 'Model': '580-5840', 'MYCT': 23, 'MMIN': 16000, 'MMAX': 32000, 'CACH': 64, 'PRP': 367, 'ERP': 381}, {'Vendor': 'amdahl', 'Model': '580-5840', 'MYCT': 23, 'MMIN': 16000, 'MMAX': 32000, 'CACH': 64, 'PRP': 489, 'ERP': 381}, {'Vendor': 'amdahl', 'Model': '580-5840', 'MYCT': 23, 'MMIN': 16000, 'MMAX': 64000, 'CACH': 64, 'PRP': 636, 'ERP': 749}, {'Vendor': 'amdahl', 'Model': '580-5840', 'MYCT': 23, 'MMIN': 32000, 'MMAX': 64000, 'CACH': 128, 'PRP': 1144, 'ERP': 1238}, {'Vendor': 'apollo', 'Model': 'dn320', 'MYCT': 400, 'MMIN': 1000, 'MMAX': 3000, 'CACH': 0, 'PRP': 38, 'ERP': 23}, {'Vendor': 'basf', 'Model': 'Jul-65', 'MYCT': 60, 'MMIN': 2000, 'MMAX': 8000, 'CACH': 65, 'PRP': 92, 'ERP': 70}, {'Vendor': 'basf', 'Model': 'Jul-68', 'MYCT': 50, 'MMIN': 4000, 'MMAX': 16000, 'CACH': 65, 'PRP': 138, 'ERP': 117}, {'Vendor': 'bti', 'Model': '5000', 'MYCT': 350, 'MMIN': 64, 'MMAX': 64, 'CACH': 0, 'PRP': 10, 'ERP': 15}, {'Vendor': 'bti', 'Model': '8000', 'MYCT': 200, 'MMIN': 512, 'MMAX': 16000, 'CACH': 0, 'PRP': 35, 'ERP': 64}, {'Vendor': 'burroughs', 'Model': 'b1955', 'MYCT': 167, 'MMIN': 524, 'MMAX': 2000, 'CACH': 8, 'PRP': 19, 'ERP': 23}, {'Vendor': 'burroughs', 'Model': 'b2900', 'MYCT': 143, 'MMIN': 512, 'MMAX': 5000, 'CACH': 0, 'PRP': 28, 'ERP': 29}, {'Vendor': 'burroughs', 'Model': 'b2925', 'MYCT': 143, 'MMIN': 1000, 'MMAX': 2000, 'CACH': 0, 'PRP': 31, 'ERP': 22}, {'Vendor': 'burroughs', 'Model': 'b4955', 'MYCT': 110, 'MMIN': 5000, 'MMAX': 5000, 'CACH': 142, 'PRP': 120, 'ERP': 124}, {'Vendor': 'burroughs', 'Model': 'b5900', 'MYCT': 143, 'MMIN': 1500, 'MMAX': 6300, 'CACH': 0, 'PRP': 30, 'ERP': 35}, {'Vendor': 'burroughs', 'Model': 'b5920', 'MYCT': 143, 'MMIN': 3100, 'MMAX': 6200, 'CACH': 0, 'PRP': 33, 'ERP': 39}, {'Vendor': 'burroughs', 'Model': 'b6900', 'MYCT': 143, 'MMIN': 2300, 'MMAX': 6200, 'CACH': 0, 'PRP': 61, 'ERP': 40}, {'Vendor': 'burroughs', 'Model': 'b6925', 'MYCT': 110, 'MMIN': 3100, 'MMAX': 6200, 'CACH': 0, 'PRP': 76, 'ERP': 45}])

    check.summary()

# Place test_return_list_correct_lenght function here
def test_return_list_correct_lenght():

    check.equal(len(load_data.add_average_main_memory(load_data.machine_vendor_list('machine-test.csv', 'apollo'))), 1)
    check.equal(len(load_data.add_average_main_memory(load_data.machine_model_list('machine-test.csv', 'b5900'))), 1)
    check.equal(len(load_data.add_average_main_memory(load_data.machine_cache_list('machine-test.csv', 32))), 12)

    check.equal(len(load_data.load_data('machine-test.csv', ('Vendor', 'basf'))), 2)
    check.equal(len(load_data.load_data('machine-test.csv', ('Model', 580 - 5840))), 0)
    check.equal(len(load_data.load_data('machine-test.csv', ('MMIN', 8000))), 0)
    check.equal(len(load_data.load_data('machine-test.csv', ('MMAX', 16000))), 0)
    check.equal(len(load_data.load_data('machine-test.csv', ('CACH', 75))), 2)
    check.equal(len(load_data.load_data('machine-test.csv', ('ERP', 45))), 0)

    check.equal(len(load_data.machine_vendor_list('machine-test.csv', 'apollo')), 1)
    check.equal(len(load_data.machine_vendor_list('machine-test.csv', 'amdahl')), 9)
    check.equal(len(load_data.machine_vendor_list('machine-test.csv', 'bti')), 2)

    check.equal(len(load_data.machine_model_list('machine-test.csv', 'Jul-68')), 1)
    check.equal(len(load_data.machine_model_list('machine-test.csv', '580-5840')), 4)
    check.equal(len(load_data.machine_model_list('machine-test.csv', '470v/0')), 0)

    check.equal(len(load_data.machine_cache_list('machine-test.csv', 0)), 22)
    check.equal(len(load_data.machine_cache_list('machine-test.csv', 142)), 1)
    check.equal(len(load_data.machine_cache_list('machine-test.csv', 6)), 13)

    check.equal(len(load_data.machine_prp_list('machine-test.csv', 10)), 22)
    check.equal(len(load_data.machine_prp_list('machine-test.csv', 318)), 5)
    check.equal(len(load_data.machine_prp_list('machine-test.csv', 777)), 1)

    check.summary()


#Place test_return_correct_dict_inside_list function here
def test_return_correct_dict_inside_list():

    # check add average main memory
    check.equal(load_data.add_average_main_memory(load_data.machine_vendor_list('machine-test.csv', 'amdahl'))
                [0], {'Model': '470v/7', 'MYCT': 29, 'MMIN': 8000, 'MMAX': 32000, 'CACH': 32, 'PRP': 269, 'ERP': 253, 'M_AVG': 20000.0})
    check.equal(load_data.add_average_main_memory(load_data.machine_vendor_list('machine-test.csv', 'amdahl'))[len(load_data.add_average_main_memory(load_data.machine_vendor_list(
        'machine-test.csv', 'amdahl'))) - 1], {'Model': '580-5840', 'MYCT': 23, 'MMIN': 32000, 'MMAX': 64000, 'CACH': 128, 'PRP': 1144, 'ERP': 1238, 'M_AVG': 48000.0})

    check.equal(load_data.add_average_main_memory(load_data.machine_vendor_list('machine-test.csv', 'amdahl'))
                [0], {'Model': '470v/7', 'MYCT': 29, 'MMIN': 8000, 'MMAX': 32000, 'CACH': 32, 'PRP': 269, 'ERP': 253, 'M_AVG': 20000.0})
    check.equal(load_data.add_average_main_memory(load_data.machine_vendor_list('machine-test.csv', 'amdahl'))
                [len(load_data.add_average_main_memory(load_data.machine_vendor_list('machine-test.csv', 'amdahl'))) - 1], {'Model': '580-5840', 'MYCT': 23, 'MMIN': 32000, 'MMAX': 64000, 'CACH': 128, 'PRP': 1144, 'ERP': 1238, 'M_AVG': 48000.0})
    check.equal(load_data.add_average_main_memory(load_data.machine_vendor_list('machine-test.csv', 'amdahl'))
                [0], {'Model': '470v/7', 'MYCT': 29, 'MMIN': 8000, 'MMAX': 32000, 'CACH': 32, 'PRP': 269, 'ERP': 253, 'M_AVG': 20000.0})
    check.equal(load_data.add_average_main_memory(load_data.machine_vendor_list('machine-test.csv', 'amdahl'))
                [len(load_data.add_average_main_memory(load_data.machine_vendor_list('machine-test.csv', 'amdahl'))) - 1], {'Model': '580-5840', 'MYCT': 23, 'MMIN': 32000, 'MMAX': 64000, 'CACH': 128, 'PRP': 1144, 'ERP': 1238, 'M_AVG': 48000.0})

    # check load data
    check.equal(load_data.load_data('machine-test.csv', ('Vendor', 'amdahl'))
                [0], {'Model': '470v/7', 'MYCT': 29, 'MMIN': 8000, 'MMAX': 32000, 'CACH': 32, 'PRP': 269, 'ERP': 253})
    check.equal(load_data.load_data('machine-test.csv', ('Vendor', 'amdahl'))[len(load_data.load_data('machine-test.csv', ('Vendor', 'amdahl'))) - 1], {
        'Model': '580-5840', 'MYCT': 23, 'MMIN': 32000, 'MMAX': 64000, 'CACH': 128, 'PRP': 1144, 'ERP': 1238})
    check.equal(load_data.load_data('machine-test.csv', ('Model', '8000'))
                [0], {'Vendor': 'bti', 'MYCT': 200, 'MMIN': 512, 'MMAX': 16000, 'CACH': 0, 'PRP': 35, 'ERP': 64})
    check.equal(load_data.load_data('machine-test.csv', ('Model', '8000'))
                [len(load_data.load_data('machine-test.csv', ('Model', '8000'))) - 1], {'Vendor': 'bti', 'MYCT': 200, 'MMIN': 512, 'MMAX': 16000, 'CACH': 0, 'PRP': 35, 'ERP': 64})
    check.equal(load_data.load_data('machine-test.csv', ('PRP', 220))
                [0], {'Vendor': 'amdahl', 'Model': '470v/7', 'MYCT': 29, 'MMIN': 8000, 'MMAX': 32000, 'CACH': 32, 'ERP': 253})
    check.equal(load_data.load_data('machine-test.csv', ('PRP', 220))
                [len(load_data.load_data('machine-test.csv', ('PRP', 220))) - 1], {'Vendor': 'amdahl', 'Model': '580-5840', 'MYCT': 23, 'MMIN': 32000, 'MMAX': 64000, 'CACH': 128, 'ERP': 1238})
    check.equal(load_data.load_data('machine-test.csv', ('Vendor', 'apollo'))
                [0], {'Model': 'dn320', 'MYCT': 400, 'MMIN': 1000, 'MMAX': 3000, 'CACH': 0, 'PRP': 38, 'ERP': 23})
    check.equal(load_data.load_data('machine-test.csv', ('Vendor', 'apollo'))[len(load_data.load_data('machine-test.csv', ('Vendor', 'apollo'))) - 1], {
        'Model': 'dn320', 'MYCT': 400, 'MMIN': 1000, 'MMAX': 3000, 'CACH': 0, 'PRP': 38, 'ERP': 23})
    check.equal(load_data.load_data('machine-test.csv', ('Model', '470v/b'))
                [0], {'Vendor': 'amdahl', 'MYCT': 26, 'MMIN': 8000, 'MMAX': 32000, 'CACH': 64, 'PRP': 318, 'ERP': 290})
    check.equal(load_data.load_data('machine-test.csv', ('Model', '470v/b'))
                [len(load_data.load_data('machine-test.csv', ('Model', '470v/b'))) - 1], {'Vendor': 'amdahl', 'MYCT': 26, 'MMIN': 8000, 'MMAX': 32000, 'CACH': 64, 'PRP': 318, 'ERP': 290})
    check.equal(load_data.load_data('machine-test.csv', ('CACH', 32))
                [0], {'Vendor': 'amdahl', 'Model': '470v/7', 'MYCT': 29, 'MMIN': 8000, 'MMAX': 32000, 'PRP': 269, 'ERP': 253})
    check.equal(load_data.load_data('machine-test.csv', ('CACH', 32))
                [len(load_data.load_data('machine-test.csv', ('CACH', 32))) - 1], {'Vendor': 'burroughs', 'Model': 'b4955', 'MYCT': 110, 'MMIN': 5000, 'MMAX': 5000, 'PRP': 120, 'ERP': 124})

    # check machine Vendor list
    check.equal(load_data.machine_vendor_list('machine-test.csv', 'amdahl')
                [0], {'Model': '470v/7', 'MYCT': 29, 'MMIN': 8000, 'MMAX': 32000, 'CACH': 32, 'PRP': 269, 'ERP': 253})
    check.equal(load_data.machine_vendor_list('machine-test.csv', 'amdahl')[len(load_data.machine_vendor_list('machine-test.csv', 'amdahl')) - 1], {
                'Model': '580-5840', 'MYCT': 23, 'MMIN': 32000, 'MMAX': 64000, 'CACH': 128, 'PRP': 1144, 'ERP': 1238})
    check.equal(load_data.machine_vendor_list('machine-test.csv', 'apollo')
                [0], {'Model': 'dn320', 'MYCT': 400, 'MMIN': 1000, 'MMAX': 3000, 'CACH': 0, 'PRP': 38, 'ERP': 23})
    check.equal(load_data.machine_vendor_list('machine-test.csv', 'apollo')
                [len(load_data.machine_vendor_list('machine-test.csv', 'apollo')) - 1], {'Model': 'dn320', 'MYCT': 400, 'MMIN': 1000, 'MMAX': 3000, 'CACH': 0, 'PRP': 38, 'ERP': 23})
    check.equal(load_data.machine_vendor_list('machine-test.csv', 'basf')
                [0], {'Model': 'Jul-65', 'MYCT': 60, 'MMIN': 2000, 'MMAX': 8000, 'CACH': 65, 'PRP': 92, 'ERP': 70})
    check.equal(load_data.machine_vendor_list('machine-test.csv', 'basf')
                [len(load_data.machine_vendor_list('machine-test.csv', 'basf')) - 1], {'Model': 'Jul-68', 'MYCT': 50, 'MMIN': 4000, 'MMAX': 16000, 'CACH': 65, 'PRP': 138, 'ERP': 117})

    # check machine Model list
    check.equal(load_data.machine_model_list('machine-test.csv', '580-5840')
                [0], {'Vendor': 'amdahl', 'MYCT': 23, 'MMIN': 16000, 'MMAX': 32000, 'CACH': 64, 'PRP': 367, 'ERP': 381})
    check.equal(load_data.machine_model_list('machine-test.csv', '580-5840')[len(load_data.machine_model_list('machine-test.csv', '580-5840')) - 1], {
        'Vendor': 'amdahl', 'MYCT': 23, 'MMIN': 32000, 'MMAX': 64000, 'CACH': 128, 'PRP': 1144, 'ERP': 1238})
    check.equal(load_data.machine_model_list('machine-test.csv', '470v/7c')
                [0], {'Vendor': 'amdahl', 'MYCT': 29, 'MMIN': 8000, 'MMAX': 16000, 'CACH': 32, 'PRP': 132, 'ERP': 132})
    check.equal(load_data.machine_model_list('machine-test.csv', '470v/7c')
                [len(load_data.machine_model_list('machine-test.csv', '470v/7c')) - 1], {'Vendor': 'amdahl', 'MYCT': 29, 'MMIN': 8000, 'MMAX': 16000, 'CACH': 32, 'PRP': 132, 'ERP': 132})
    check.equal(load_data.machine_model_list('machine-test.csv', 'b2900')
                [0], {'Vendor': 'burroughs', 'MYCT': 143, 'MMIN': 512, 'MMAX': 5000, 'CACH': 0, 'PRP': 28, 'ERP': 29})
    check.equal(load_data.machine_model_list('machine-test.csv', 'b2900')
                [len(load_data.machine_model_list('machine-test.csv', 'b2900')) - 1], {'Vendor': 'burroughs', 'MYCT': 143, 'MMIN': 512, 'MMAX': 5000, 'CACH': 0, 'PRP': 28, 'ERP': 29})

    # check machine cache list
    check.equal(load_data.machine_cache_list('machine-test.csv', 32)
                [0], {'Vendor': 'amdahl', 'Model': '470v/7', 'MYCT': 29, 'MMIN': 8000, 'MMAX': 32000, 'PRP': 269, 'ERP': 253})
    check.equal(load_data.machine_cache_list('machine-test.csv', 32)[len(load_data.machine_cache_list('machine-test.csv', 32)) - 1], {
        'Vendor': 'burroughs', 'Model': 'b4955', 'MYCT': 110, 'MMIN': 5000, 'MMAX': 5000, 'PRP': 120, 'ERP': 124})
    check.equal(load_data.machine_cache_list('machine-test.csv', 64)
                [0], {'Vendor': 'amdahl', 'Model': '470v/b', 'MYCT': 26, 'MMIN': 8000, 'MMAX': 32000, 'PRP': 318, 'ERP': 290})
    check.equal(load_data.machine_cache_list('machine-test.csv', 64)
                [len(load_data.machine_cache_list('machine-test.csv', 64)) - 1], {'Vendor': 'burroughs', 'Model': 'b4955', 'MYCT': 110, 'MMIN': 5000, 'MMAX': 5000, 'PRP': 120, 'ERP': 124})
    check.equal(load_data.machine_cache_list('machine-test.csv', 0)
                [0], {'Vendor': 'amdahl', 'Model': '470v/7', 'MYCT': 29, 'MMIN': 8000, 'MMAX': 32000, 'PRP': 269, 'ERP': 253})
    check.equal(load_data.machine_cache_list('machine-test.csv', 0)
                [len(load_data.machine_cache_list('machine-test.csv', 0)) - 1], {'Vendor': 'burroughs', 'Model': 'b6925', 'MYCT': 110, 'MMIN': 3100, 'MMAX': 6200, 'PRP': 76, 'ERP': 45})

    # check machine prp list
    check.equal(load_data.machine_prp_list('machine-test.csv', 269)
                [0], {'Vendor': 'amdahl', 'Model': '470v/7', 'MYCT': 29, 'MMIN': 8000, 'MMAX': 32000, 'CACH': 32, 'ERP': 253})
    check.equal(load_data.machine_prp_list('machine-test.csv', 269)[len(load_data.machine_prp_list('machine-test.csv', 269)) - 1], {
        'Vendor': 'amdahl', 'Model': '580-5840', 'MYCT': 23, 'MMIN': 32000, 'MMAX': 64000, 'CACH': 128, 'ERP': 1238})
    check.equal(load_data.machine_prp_list('machine-test.csv', 381)
                [0], {'Vendor': 'amdahl', 'Model': '580-5840', 'MYCT': 23, 'MMIN': 16000, 'MMAX': 32000, 'CACH': 64, 'ERP': 381})
    check.equal(load_data.machine_prp_list('machine-test.csv', 381)
                [len(load_data.machine_prp_list('machine-test.csv', 381)) - 1], {'Vendor': 'amdahl', 'Model': '580-5840', 'MYCT': 23, 'MMIN': 32000, 'MMAX': 64000, 'CACH': 128, 'ERP': 1238})
    check.equal(load_data.machine_prp_list('machine-test.csv', 22)
                [0], {'Vendor': 'amdahl', 'Model': '470v/7', 'MYCT': 29, 'MMIN': 8000, 'MMAX': 32000, 'CACH': 32, 'ERP': 253})
    check.equal(load_data.machine_prp_list('machine-test.csv', 22)
                [len(load_data.machine_prp_list('machine-test.csv', 22)) - 1], {'Vendor': 'burroughs', 'Model': 'b6925', 'MYCT': 110, 'MMIN': 3100, 'MMAX': 6200, 'CACH': 0, 'ERP': 45})

    # check tests passed
    check.summary()

#Place test_add_average function here
def test_add_average():

    # 'Model' is not a key of the dictionary
    machines1 = [{'Vendor': 'amdahl', 'MYCT': 29, 'MMIN': 8000, 'MMAX': 32000, 'CACH': 32, 'PRP': 269, 'ERP': 253}]
    load_data.add_average_main_memory(machines1)
    check.equal(len(machines1), 1)
    check.equal(len(machines1[0]), 8)
    check.equal(machines1[0]['M_AVG'], 20000.0)

    # 'Vendor' is not a key of the dictionary
    machines2 = [{'Model': '470v/7c', 'MYCT': 29, 'MMIN': 8000, 'MMAX': 16000, 'CACH': 32, 'PRP': 132, 'ERP': 132}]
    load_data.add_average_main_memory(machines2)
    check.equal(len(machines2), 1)
    check.equal(len(machines2[0]), 8)
    check.equal(machines2[0]['M_AVG'], 12000.0)

    # 'CACH' is not a key of the dictionary
    machines3 = [{'Vendor': 'amdahl', 'Model': '470v/7', 'MYCT': 29, 'MMIN': 8000, 'MMAX': 32000, 'PRP': 269, 'ERP': 253}]
    load_data.add_average_main_memory(machines3)
    check.equal(len(machines3), 1)
    check.equal(len(machines3[0]), 8)
    check.equal(machines3[0]['M_AVG'], 20000.0)

    # 'PRP' is not a key of the dictionary
    machines4 = [{'Vendor': 'amdahl', 'Model': '470v/7', 'MYCT': 29, 'MMIN': 8000, 'MMAX': 32000, 'CACH': 32, 'ERP': 253}]
    load_data.add_average_main_memory(machines4)
    check.equal(len(machines4), 1)
    check.equal(len(machines4[0]), 8)
    check.equal(machines4[0]['M_AVG'], 20000.0)

    # All keys are present
    machines5 = [{'Vendor': 'amdahl', 'Model': '470v/7', 'MYCT': 29, 'MMIN': 8000, 'MMAX': 32000, 'CACH': 32, 'PRP': 269, 'ERP': 253}]
    load_data.add_average_main_memory(machines5)
    check.equal(len(machines5), 1)
    check.equal(len(machines5[0]), 9)
    check.equal(machines5[0]['M_AVG'], 20000.0)

    # List is empty
    machines6 = []
    load_data.add_average_main_memory(machines6)
    check.equal(len(machines6), 0)

    check.summary()


# Do NOT include a main script in your submission
