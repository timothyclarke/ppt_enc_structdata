class enc_example
(
    $data
){
    enc_example::software { $data['software'] :
        versions => $data['versions'],
    }
}
