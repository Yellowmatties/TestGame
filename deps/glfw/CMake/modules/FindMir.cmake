if (NOT WIN32)

  find_package (PkgConfig)
  pkg_check_modules (PKG_MIR QUIET mirclient)

  set (MIR_INCLUDE_DIR ${PKG_MIR_INCLUDE_DIRS})
  set (MIR_LIBRARIES   ${PKG_MIR_LIBRARIES})

endif ()
