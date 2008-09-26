Summary:	A library to access memcache
Name:		ruby-memcache-client
Version:	1.5.0
Release:	1
License:	Ruby's
Group:		Development/Languages
Source0:	http://gems.rubyforge.org/gems/memcache-client-%{version}.gem
# Source0-md5:	97a8bc54c781cb34d951889ac7c0e9bc
#Patch0: %{name}-nogems.patch
URL:		http://seattlerb.rubyforge.org/memcache-client/
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	setup.rb = 3.4.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%prep
%setup -q -c
tar xf %{SOURCE0} -O data.tar.gz | tar xzv-
#%patch0 -p1
cp %{_datadir}/setup.rb .

%build
ruby setup.rb config \
	--rbdir=%{ruby_rubylibdir} \
	--sodir=%{ruby_archdir}

ruby setup.rb setup

rdoc --op rdoc lib
rdoc --ri --op ri lib

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_archdir},%{ruby_ridir}}

ruby setup.rb install \
	--prefix=$RPM_BUILD_ROOT

cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc rdoc
%{ruby_rubylibdir}/memcache.rb
%{ruby_rubylibdir}/memcache_util.rb
