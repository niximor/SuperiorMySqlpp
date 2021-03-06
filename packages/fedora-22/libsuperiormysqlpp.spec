Name:           libsuperiormysqlpp-dev
Version:        0.1.2
Release:        development%{?dist}
Summary:        C++ mysql library development files

License:        LGPLv3+
URL:            http://ftp.gnu.org/gnu/%{name}
Source0:        http://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz

BuildRequires:  docker, gcc-c++, community-mysql-devel, hostname, libasan, libubsan, tree
      
Requires(post): info
Requires(preun): info

%description 
C++ mysql library development files

%prep

%build

%check
make -j -B test

%install
make -j install VERSION=%{version} DESTDIR=%{buildroot} prefix=/usr

%clean
make -j clean package-fedora-22-clean

%post

%preun

%files 
/usr/include/*

