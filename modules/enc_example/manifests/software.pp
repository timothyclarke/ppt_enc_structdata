define enc_example::software
(
    $versions,
){
    notify { "${name} should be ${versions[$name]}" : }


}
