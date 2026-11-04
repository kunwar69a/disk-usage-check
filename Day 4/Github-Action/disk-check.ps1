param(
    [int]$ThresholdPercent = 20
)

$drives = Get-CimInstance Win32_LogicalDisk -Filter "DriveType=3"

foreach ($drive in $drives) {
    $freePercent = [math]::Round(($drive.FreeSpace / $drive.Size) * 100, 1)

    Write-Output "$($drive.DeviceID) has $freePercent% free"

    if ($freePercent -lt $ThresholdPercent) {
        Write-Warning "$($drive.DeviceID) is below the $ThresholdPercent% free-space threshold"
    }
}
if ()