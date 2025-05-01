<#
.SYNOPSIS
Get-networkAdapter Retrieves network adapter information from one or more computers.
.DESCRIPTION
s.ps1 uses WMI to retrieve win32_networkadapter instances from one or more computers. 
Displaying their
.PARAMETER computername
This is the computer name to query, can use multiple or saved pssessions for remote access for example,
Default: Localhost (ourPc)
.PARAMETER drivetype
This displays drives 2 or 3 are the options, this can be altered
.EXAMPLE
.\s.ps1 -computername localhost -DeviceID 2 -Verbose
#>

[CmdletBinding()]
param (
    [Parameter(Mandatory=$True, HelpMessage="Enter computer name here")]
    [Alias('host')]
    [string]$computername,
    
    
    [ValidateSet(2,3)]
    [Parameter(Mandatory =$True)]
    [int]$DeviceID 
)


Write-Verbose "Connecting to network adapter under entered computer name: $computername"
Write-Verbose "Looking for device type $deviceID"
Get-CimInstance win32_networkadapter -ComputerName localhost |
Where-Object { $_.PhysicalAdapter } |
Select-Object MACAddress,AdapterType,DeviceID,Name,Speed
Write-Verbose "Finished output"
