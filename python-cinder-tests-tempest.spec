%{!?sources_gpg: %{!?dlrn:%global sources_gpg 1} }
%global sources_gpg_sign 0x01527a34f0d0080f8a5db8d6eb6c5df21b4b6363
%global service cinder
%global plugin cinder-tempest-plugin
%global module cinder_tempest_plugin

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%global common_desc \
This package contains Tempest tests to cover the cinder project. \
Additionally it provides a plugin to automatically load these tests \
into Tempest.

Name:       python-%{service}-tests-tempest
Version:    1.6.0
Release:    1%{?dist}
Summary:    Tempest Integration of Cinder Project
License:    ASL 2.0
URL:        https://git.openstack.org/cgit/openstack/%{plugin}/

Source0:    http://tarballs.openstack.org/%{plugin}/%{plugin}-%{upstream_version}.tar.gz
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101:        http://tarballs.openstack.org/%{plugin}/%{plugin}-%{upstream_version}.tar.gz.asc
Source102:        https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif

BuildArch:  noarch

# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
BuildRequires:  /usr/bin/gpgv2
%endif

BuildRequires:  git-core
BuildRequires:  openstack-macros

%description
%{common_desc}

%package -n python3-%{service}-tests-tempest
Summary: %{summary}
%{?python_provide:%python_provide python3-%{service}-tests-tempest}
BuildRequires:  python3-devel
BuildRequires:  python3-pbr
BuildRequires:  python3-setuptools

Obsoletes:   python-cinder-tests < 1:12.0.0

Requires:   python3-pbr >= 3.1.1
Requires:   python3-six >= 1.10.0
Requires:   python3-tempest >= 1:18.0.0
Requires:   python3-oslo-config >= 2:5.2.0
Requires:   python3-oslo-serialization >= 2.18.0

%description -n python3-%{service}-tests-tempest
%{common_desc}

%prep
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
%autosetup -n %{plugin}-%{upstream_version} -S git

# Let's handle dependencies ourseleves
%py_req_cleanup
# Remove bundled egg-info
rm -rf %{module}.egg-info

%build
%{py3_build}

%install
%{py3_install}

%files -n python3-%{service}-tests-tempest
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{module}
%{python3_sitelib}/*.egg-info

%changelog
* Fri Apr 08 2022 RDO <dev@lists.rdoproject.org> 1.6.0-1
- Update to 1.6.0

* Wed Sep 29 2021 RDO <dev@lists.rdoproject.org> 1.5.0-1
- Update to 1.5.0

