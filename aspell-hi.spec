%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

%define src_ver 0.02-0
%define fname aspell6-%{languagecode}
%define aspell_ver 0.60
%define languageenglazy Hindi
%define languagecode hi
%define lc_ctype hi_IN

Summary:       %{languageenglazy} files for aspell
Name:          aspell-%{languagecode}
Version:       0.02.0
Release:       %mkrel 8
Group:         System/Internationalization
Source:        http://ftp.gnu.org/gnu/aspell/dict/%{languagecode}/%{fname}-%{src_ver}.tar.bz2
Patch1:		hindu-specific-chars.patch
URL:		   http://aspell.net/
License:	   GPL
BuildRoot:     %{_tmppath}/%{name}-%{version}-root
Provides: spell-%{languagecode}

BuildRequires: aspell >= %{aspell_ver}
BuildRequires: make
Requires:      aspell >= %{aspell_ver}

# Mandriva Stuff
Requires:      locales-%{languagecode}
# aspell = 1, myspell = 2, lang-specific = 3
Provides:      enchant-dictionary = 1
Provides:      aspell-dictionary
Provides:      aspell-%{lc_ctype}

Autoreqprov:   no

%description
An %{languageenglazy} dictionary for use with aspell, a spelling checker.

%prep
%setup -q -n %{fname}-%{src_ver}
%patch1 -p0
mv u-deva.cset u-deva-hi.cset
mv u-deva.cmap u-deva-hi.cmap

%build
# don't use configure macro
./configure

%make

%install
rm -fr $RPM_BUILD_ROOT

%makeinstall_std

chmod 644 Copyright README* 

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc Copyright README*
%{_libdir}/aspell-%{aspell_ver}/*




%changelog
* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 0.02.0-8mdv2011.0
+ Revision: 662835
- mass rebuild

* Mon Nov 29 2010 Oden Eriksson <oeriksson@mandriva.com> 0.02.0-7mdv2011.0
+ Revision: 603215
- rebuild

* Sun Mar 14 2010 Oden Eriksson <oeriksson@mandriva.com> 0.02.0-6mdv2010.1
+ Revision: 518928
- rebuild

  + Isabel Vallejo <isabel@mandriva.org>
    - Add patch to make aspell-hi and aspell-mr installable at the same time

* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 0.02.0-4mdv2010.0
+ Revision: 413071
- rebuild

* Fri Mar 06 2009 Antoine Ginies <aginies@mandriva.com> 0.02.0-3mdv2009.1
+ Revision: 350033
- 2009.1 rebuild

* Wed Aug 06 2008 Thierry Vignaud <tv@mandriva.org> 0.02.0-2mdv2009.0
+ Revision: 264322
- rebuild early 2009.0 package (before pixel changes)

* Fri Apr 25 2008 Funda Wang <fwang@mandriva.org> 0.02.0-1mdv2009.0
+ Revision: 197368
- New version 0.02

* Sun Mar 09 2008 Anssi Hannula <anssi@mandriva.org> 0.01.0-5mdv2008.1
+ Revision: 182464
- provide enchant-dictionary

* Fri Jan 11 2008 Thierry Vignaud <tv@mandriva.org> 0.01.0-4mdv2008.1
+ Revision: 148791
- rebuild
- kill re-definition of %%buildroot on Pixel's request
- s/Mandrake/Mandriva/

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Wed Feb 21 2007 Oden Eriksson <oeriksson@mandriva.com> 0.01.0-3mdv2007.0
+ Revision: 124100
- rebuilt due to bs fjukiness
- Import aspell-hi

* Wed Feb 21 2007 Oden Eriksson <oeriksson@mandriva.com> 0.01.0-2mdv2007.1
- use the mkrel macro
- disable debug packages

* Wed Feb 16 2005 Pablo Saratxaga <pablo@mandrakesoft.com> 0.01.0-1mdk
- first version

