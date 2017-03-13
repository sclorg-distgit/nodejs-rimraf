%{?scl:%scl_package nodejs-rimraf}
%{!?scl:%global pkg_name %{name}}
%{?nodejs_find_provides_and_requires}

Name:       %{?scl_prefix}nodejs-rimraf
Version:    2.5.2
Release:    2%{?dist}
Summary:    A deep deletion module for node.js
License:    ISC
URL:        https://github.com/isaacs/rimraf
Source0:    http://registry.npmjs.org/rimraf/-/rimraf-%{version}.tgz
BuildArch:  noarch
ExclusiveArch: %{nodejs_arches} noarch

BuildRequires:  %{?scl_prefix}nodejs-devel

%description
%summary (like `rm -rf`).

%prep
%setup -q -n package

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/rimraf
cp -pr bin.js rimraf.js package.json %{buildroot}%{nodejs_sitelib}/rimraf

%nodejs_symlink_deps

%check
#tests now requires tap, disabling them

%files
%{nodejs_sitelib}/rimraf
%doc LICENSE README.md

%changelog
* Thu Jun 09 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 2.5.2-2
- Resolves: rhbz#1334856 , fixes wrong license

* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 2.5.2-1
- Update

* Mon Nov 30 2015 Tomas Hrcka <thrcka@redhat.com> - 2.4.3-1
- Rebase to latest upstream

* Thu Jan 08 2015 Tomas Hrcka <thrcka@redhat.com> - 2.2.8-1
- New upstream release 2.2.8

* Thu Jan 16 2014 Tomas Hrcka <thrcka@redhat.com> - 2.2.6-1
- New upstream release 2.2.6

* Thu Oct 17 2013 Tomas Hrcka <thrcka@redhat.com> - 2.2.2-2
- replace provides and requires with macro


* Tue Jul 30 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 2.2.2-1
- new upstream release 2.2.2

* Sun Jun 23 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 2.2.0-1
- new upstream release 2.2.0

* Sat Jun 22 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 2.1.4-3
- restrict to compatible arches

* Mon Apr 15 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 2.1.4-2
- add macro for EPEL6 dependency generation

* Thu Apr 11 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.1.4-2
- Add support for software collections

* Sat Feb 09 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 2.1.4-1
- new upstream release 2.1.4

* Tue Jan 08 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 2.1.1-2
- add missing build section

* Mon Dec 31 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 2.1.1-1
- new upstream release 2.1.1
- clean up for submission

* Fri Apr 27 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 2.0.1-2
- guard Requires for F17 automatic depedency generation

* Thu Feb 09 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 2.0.1-1
- new upstream release 2.0.1

* Tue Oct 25 2011 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.9-1
- new upstream release

* Tue Aug 23 2011 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.3-1
- initial package
