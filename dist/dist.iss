; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

[Setup]
; NOTE: The value of AppId uniquely identifies this application. Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{45D2AA68-4346-4550-90D4-7F0A1C344B9F}
AppName=AspazIA
AppVersion=0.1
;AppVerName=AspazIA 0.1
AppPublisher=AndreisPurim
AppPublisherURL=https://andreispurim.github.io/
AppSupportURL=https://andreispurim.github.io/
AppUpdatesURL=https://andreispurim.github.io/
DefaultDirName={autopf}\AspazIA
DisableProgramGroupPage=yes
; Uncomment the following line to run in non administrative install mode (install for current user only.)
;PrivilegesRequired=lowest
PrivilegesRequiredOverridesAllowed=dialog
OutputBaseFilename=mysetup
Compression=lzma
SolidCompression=yes
WizardStyle=modern

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "C:\Users\Micro\Desktop\aspazIA\dist\aspazia.exe"; DestDir: "{app}"; Flags: ignoreversion
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Icons]
Name: "{autoprograms}\AspazIA"; Filename: "{app}\aspazia.exe"
Name: "{autodesktop}\AspazIA"; Filename: "{app}\aspazia.exe"; Tasks: desktopicon

[Run]
Filename: "{app}\aspazia.exe"; Description: "{cm:LaunchProgram,AspazIA}"; Flags: nowait postinstall skipifsilent

