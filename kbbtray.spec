Summary: Display the status of a Big Brother or Hobbit page in the system tray
Name: kbbtray
Version: 0.07
Release: %mkrel 3
License: GPL
Group: Monitoring
BuildArch: noarch
URL: http://coldstonelabs.org/doku.php?id=software:kbbtray
Source: http://coldstonelabs.org/files/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: python-kde

%description
Kbbtray displays the status of a Big Brother or Hobbit page in the system tray.
It's written in Python and uses PyKDE.

%prep
%setup -q

%build

%install
%{__rm} -rf %{buildroot}
sed -i "s|/usr/local|%{buildroot}%{_prefix}|g" install.sh
sed -i "s|/bin/install|%{__install}|g" install.sh
perl -pi -e 's/-o root//g;s/-g root//g;' install.sh
sed -i "s|/usr/local|%{_prefix}|g" kbbtray.py
%{__mkdir_p} %{buildroot}%{_bindir}
./install.sh

install -d %{buildroot}/%{_datadir}/applications
cat <<EOF >> %{buildroot}/%{_datadir}/applications/%{name}.desktop
[Desktop Entry]
Encoding=UTF-8
Name=KBBTray
Comment=Hobbit/BigBrother tray monitor
Exec=%{_bindir}/kbbtray.py
Icon=/usr/share/kbbtray/green.png
Terminal=false
Type=Application
Categories=Qt;KDE;X-MandrivaLinux-System-Monitoring;System;Monitor;
EOF

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING README REAL-BB-ICONS TODO
%{_bindir}/kbbtray.py
%{_datadir}/kbbtray/
%{_datadir}/applications/%{name}.desktop

