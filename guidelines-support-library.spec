# Set Git revision of library...
%global commit0 1c95f9436eae69c9b9315911ef6aa210df7d1e31
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global date 20171014

Name: guidelines-support-library
Summary: Guidelines Support Library
Version: 0
Release: 1.%{date}git%{shortcommit0}%{?dist}

License: MIT
URL: https://github.com/Microsoft/GSL
Source0: %{url}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
BuildArch: noarch

%description
Header-only %{summary}.

%package devel
Summary: Development files for %{name}
Provides: %{name}-static = %{version}-%{release}

%description devel
%{summary}.

%prep
%autosetup -n GSL-%{commit0} -p1

%build
# Nothing to build. Header-only library.

%install
# Installing headers...
mkdir -p "%{buildroot}%{_includedir}/%{name}/gsl"
cp -a include/gsl %{buildroot}%{_includedir}/%{name}

%files devel
%doc README.md CONTRIBUTING.md
%license LICENSE ThirdPartyNotices.txt
%{_includedir}/%{name}

%changelog
* Tue Nov 28 2017 Vitaly Zaitsev <vitaly@easycoding.org> - 0-1.20171014git1c95f94
- Initial SPEC release. 
