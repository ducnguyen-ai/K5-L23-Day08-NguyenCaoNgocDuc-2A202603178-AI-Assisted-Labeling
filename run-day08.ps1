param(
    [Parameter(Position=0)][ValidateSet('check','script')][string]$Action='check',
    [Parameter(Position=1)][string]$Script,
    [Parameter(ValueFromRemainingArguments=$true)][string[]]$ScriptArgs
)
$ErrorActionPreference='Stop'
$env:PYTHONUTF8='1'
$python=Join-Path $PSScriptRoot '.venv\Scripts\python.exe'
Push-Location $PSScriptRoot
try {
    if($Action -eq 'check') {
        & $python scripts/check_env.py --cvat http://localhost:8081
    } else {
        if([IO.Path]::GetFileName($Script) -ne $Script -or $Script -notlike '*.py') { throw 'Chỉ nhận tên script .py trong scripts/.' }
        $target=Join-Path $PSScriptRoot "scripts\$Script"
        if(-not(Test-Path -LiteralPath $target -PathType Leaf)){throw "Không tìm thấy $Script"}
        if($Script -in @('prelabel.py','sam2_points.py') -and -not(Test-Path 'submission/labels/gold_manual.json')){
            throw 'Cần hoàn thành và xuất gold_manual.json trước khi chạy model theo RULES.md. Xem START_HERE.md.'
        }
        & $python $target @ScriptArgs
    }
    $result=$LASTEXITCODE
} finally { Pop-Location }
exit $result
