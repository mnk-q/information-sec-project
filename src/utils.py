def load_datasets():
    # load test data 
    test_data_dirs = {
        #'train_Conv' :'./data/target/train_conversion/',
        #'test'       :'./data/target/test/',
        #'ubg_test'   :'./data/ubg/test/',
        #'fake'       :'./data/fake'
    }
    voice_dirs = {'fake{}'.format(50*n):'./model/conversion/pretrained/validation_output/converted_B_{}epc'.format(50*n) for n in range(21)}
    test_data_dirs.update(voice_dirs)
    test_data = {}
    for name, data_dir in test_data_dirs.items():
        test_data[name] =load_wavs_as_matrices(data_dir)
        
    return test_data