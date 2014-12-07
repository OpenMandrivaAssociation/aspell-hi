%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

%define src_ver 0.02-0
%define fname aspell6-%{languagecode}
%define aspell_ver 0.60
%define languageenglazy Hindi
%define languagecode hi
%define lc_ctype hi_IN

Summary:	%{languageenglazy} files for aspell
Name:		aspell-%{languagecode}
Version:	0.02.0
Release:	15
Group:		System/Internationalization
Url:		http://aspell.net/
License:	GPLv2
Source0:	http://ftp.gnu.org/gnu/aspell/dict/%{languagecode}/%{fname}-%{src_ver}.tar.bz2
Patch1:		hindu-specific-chars.patch

BuildRequires:	aspell >= %{aspell_ver}
Requires:	aspell >= %{aspell_ver}
# Mandriva Stuff
Requires:	locales-%{languagecode}
# aspell = 1, myspell = 2, lang-specific = 3
Provides:	enchant-dictionary = 1
Provides:	aspell-dictionary
Provides:	aspell-%{lc_ctype}
Provides:	spell-%{languagecode}
Autoreqprov:	no

%description
An %{languageenglazy} dictionary for use with aspell, a spelling checker.

%prep
%setup -qn %{fname}-%{src_ver}
%patch1 -p0
mv u-deva.cset u-deva-hi.cset
mv u-deva.cmap u-deva-hi.cmap

%build
# don't use configure macro
./configure

%make

%install
%makeinstall_std

chmod 644 Copyright README* 

%files
%doc Copyright README*
%{_libdir}/aspell-%{aspell_ver}/*

