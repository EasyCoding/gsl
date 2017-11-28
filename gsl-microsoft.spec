# Disable debug package...
%global debug_package %{nil}

# Set Git revision of library...
%global commit0 1c95f9436eae69c9b9315911ef6aa210df7d1e31
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global date 20171014

Name: gsl-microsoft
Summary: Guidelines Support Library
Version: 0
Release: 1.%{date}git%{shortcommit0}%{?dist}

License: MIT
URL: https://github.com/Microsoft/GSL
Source0: %{url}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

%description
Header-only %{release}.

%package devel
Summary: Development files for %{name}

%description devel
%{summary}.

%prep
%autosetup -n GSL-%{commit0} -p1

%build
# Nothing to build. Header-only library.

%install
# Installing headers...
mkdir -p "%{buildroot}%{_includedir}/%{name}/gsl"
find include/gsl -maxdepth 1 -type f -name "*" -exec install -m 0644 -p '{}' %{buildroot}%{_includedir}/%{name}/gsl \;

%files devel
%doc README.md CONTRIBUTING.md
%license LICENSE ThirdPartyNotices.txt
%{_includedir}/%{name}

%changelog
* Tue Nov 28 2017 Vitaly Zaitsev <vitaly@easycoding.org> - 0-1.20171014git1c95f94
- Initial SPEC release.

 
