$UDPClient = New-Object System.Net.Sockets.UdpClient
$UDPClient.Connect("192.168.1.43", 514)

# Mensagem de teste no formato do Mikrotik
$Message = "<134>input accept in:ether1 out:ether2, proto tcp, 192.168.1.1:12345->8.8.8.8:80, len 60"
$MessageBytes = [System.Text.Encoding]::ASCII.GetBytes($Message)

Write-Host "Enviando mensagem de teste..."
$UDPClient.Send($MessageBytes, $MessageBytes.Length)
Write-Host "Mensagem enviada!"

$UDPClient.Close() 