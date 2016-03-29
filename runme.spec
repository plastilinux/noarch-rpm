%define __jar_repack %{nil}
Name: runme
Version: 1
Release: 1
Summary: Example set of files
BuildArch: noarch
License: GPL
URL: http://plastilinux.blogspot.com
Source0: runscripts.tgz
Source1: README.txt
Source2: runme.sh

%description
Example noarch rpm

%install
mkdir -p %{buildroot}/opt/runme
tar -C %{buildroot}/opt/runme -xf %SOURCE0
install -m 644 %SOURCE1 %{buildroot}/opt/runme
install -m 755 %SOURCE2 %{buildroot}/opt/runme

%files
%defattr(-, root, root)
%dir /opt/runme
%dir /opt/runme/runscripts.d
/opt/runme/README.txt
%attr(755,root,root) /opt/runme/runme.sh
%attr(755,root,root) /opt/runme/runscripts.d/*


%changelog

